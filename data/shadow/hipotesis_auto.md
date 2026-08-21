# Hipótesis automáticas — 2026-08-21 18:12 UTC
_Generado por shadow_postmortem.py sobre 104155 resoluciones (PNL=+8581.85€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.174 (n=84)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.264 (n=172)

- **FILTRO** `banda_hit_calibrado` < `0.7988` → IC=-0.174 (n=84)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.7988
  - _Potencial_: sin este filtro IC_bueno=+0.264 (n=172)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=215)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.264 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.120)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.132 (n=180)

  - _Acción_: Kelly boost +0.66€ cuando `n_ballena_banda` > 20.0 (IC base=+0.120)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.233 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.120)

- **PATRÓN** `banda_hit_calibrado` > `0.7988` → IC=+0.264 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7988 (IC base=+0.120)

- **PATRÓN** `banda_z` > `9.867` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.867 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=200)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `3111.6433` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3111.6433 (IC base=+0.120)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.018)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `banda_hit_calibrado` < `0.8014` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8014
  - _Potencial_: sin este filtro IC_bueno=+0.286 (n=96)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.338 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=113)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.153)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.170 (n=98)

  - _Acción_: Kelly boost +0.85€ cuando `n_ballena_banda` > 26.0 (IC base=+0.153)

- **PATRÓN** `n_total_lado` > `71.0` → IC=+0.260 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 71.0 (IC base=+0.153)

- **PATRÓN** `banda_z` > `10.085` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 10.085 (IC base=+0.153)

- **PATRÓN** `ballenas_wallet_edge_medio` > `1.275` → IC=+0.174 (n=90)

  - _Acción_: Kelly boost +0.87€ cuando `ballenas_wallet_edge_medio` > 1.275 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.167 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 4.0 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `4634.0182` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4634.0182 (IC base=+0.153)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.013)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.193 (n=86)

- **FILTRO** `banda_hit_calibrado` < `0.6284` → IC=-0.218 (n=37)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6284
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=77)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=90)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=69)

- **FILTRO** `n_ballena_banda` < `30.0` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `n_ballena_banda` < 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=52)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.335 (IC base=+0.078)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.078)

- **PATRÓN** `banda_z` > `8.174` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `banda_z` > 8.174 (IC base=+0.078)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.078)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `156.21` → IC=-0.263 (n=1469)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.21
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4408)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `n_ballenas` < `4.0` → IC=-0.150 (n=370)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=214)

- **FILTRO** `restante_s_al_confirmar` < `133.51` → IC=-0.318 (n=146)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.51
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=438)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `639.7` → IC=-0.243 (n=138)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 639.7
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=418)

- **FILTRO** `restante_s_al_confirmar` < `374.92` → IC=-0.259 (n=139)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 374.92
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=417)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `86.19` → IC=-0.446 (n=166)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 86.19
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=500)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `140.8` → IC=-0.242 (n=347)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.8
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=1042)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `170.62` → IC=-0.328 (n=382)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 170.62
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=778)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.190 (n=3534)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=1301)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2373.8543` → IC=+0.170 (n=1254)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2373.8543 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=2212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=2719)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.264 (n=2045)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=2304)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4254.3438` → IC=+0.173 (n=960)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4254.3438 (IC base=+0.132)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.381 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.294 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=559)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.189)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.162 (n=386)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.6` → IC=+0.185 (n=195)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.6 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5033.4098` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5033.4098 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.198 (n=170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` < `0.39` → IC=+0.202 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.39 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5212.6993` → IC=+0.158 (n=226)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 5212.6993 (IC base=+0.136)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.136 (n=770)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.308 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.299 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=332)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.412 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `2484.3963` → IC=+0.311 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2484.3963 (IC base=+0.289)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.173 (n=255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.248 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.150 (n=358)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2108.3856` → IC=+0.169 (n=288)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2108.3856 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.160 (n=139)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4420.281 (IC base=+0.085)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.202 (n=471)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.434 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.259 (n=143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` < `0.31` → IC=+0.318 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.31 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.233 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `748.2618` → IC=+0.241 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 748.2618 (IC base=+0.214)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.260 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.195 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 8.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.350 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.186)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.219 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.158 (n=261)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.103)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=77)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=108)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=3338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=2929)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.203 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.166 (n=564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.174 (n=842)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.186 (n=839)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.74 (IC base=+0.165)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.795` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=34)

- **FILTRO** `libro_liquidez` < `8910.53` → IC=-0.330 (n=45)

  - _Acción_: SKIP cuando `libro_liquidez` < 8910.53
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.326)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.326)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=853)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.176 (n=369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 7.0 (IC base=+0.159)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.183 (n=291)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.7 (IC base=+0.159)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.164 (n=468)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.73 (IC base=+0.159)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.230 (n=662)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.319 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

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
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.199 (n=350)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 7.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.192 (n=828)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.74 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.444 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `3965.0747` → IC=+0.449 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3965.0747 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.429 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `9836.4076` → IC=+0.467 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9836.4076 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `4.0` → IC=+0.426 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.402 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.939` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.939 (IC base=+0.409)

- **PATRÓN** `libro_liquidez` > `2077.5174` → IC=+0.433 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2077.5174 (IC base=+0.409)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.419 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.447 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.92` → IC=+0.423 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.92 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.421 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.426)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=7220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.199 (n=4789)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.227 (n=5241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.136 (n=896)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 11.0 (IC base=+0.116)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.161 (n=954)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.71 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.270 (n=380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.285 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.240)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.158 (n=604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.163 (n=835)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 11.0 (IC base=+0.157)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.204 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.157)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.247 (n=1012)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.241 (n=819)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.311 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.241)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=1029)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.273 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.237)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.228 (n=424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.201 (n=804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.237 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.204 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.131)

- **PATRÓN** `restante_min` < `3.87` → IC=+0.163 (n=858)

  - _Acción_: Kelly boost +0.81€ cuando `restante_min` < 3.87 (IC base=+0.131)

- **PATRÓN** `restante_min` > `4.92` → IC=+0.149 (n=854)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.92 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.145 (n=1852)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 12.0 (IC base=+0.131)

- **PATRÓN** `lag_apertura_s` < `5.09` → IC=+0.149 (n=854)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 5.09 (IC base=+0.131)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.226 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.144)

- **PATRÓN** `restante_min` < `3.77` → IC=+0.183 (n=427)

  - _Acción_: Kelly boost +0.91€ cuando `restante_min` < 3.77 (IC base=+0.144)

- **PATRÓN** `restante_min` > `4.89` → IC=+0.158 (n=440)

  - _Acción_: Kelly boost +0.79€ cuando `restante_min` > 4.89 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.163 (n=916)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 12.0 (IC base=+0.144)

- **PATRÓN** `lag_apertura_s` < `6.72` → IC=+0.165 (n=425)

  - _Acción_: Kelly boost +0.83€ cuando `lag_apertura_s` < 6.72 (IC base=+0.144)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.181 (n=472)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.37 (IC base=+0.118)

- **PATRÓN** `restante_min` < `3.95` → IC=+0.141 (n=435)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` < 3.95 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.159 (n=435)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` > 4.95 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.124 (n=1321)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 17.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `3.28` → IC=+0.160 (n=430)

  - _Acción_: Kelly boost +0.80€ cuando `lag_apertura_s` < 3.28 (IC base=+0.118)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.311 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.311 (n=432)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.386 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.301)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.283 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.287 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` < `0.725` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.725 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.353 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5730.9756` → IC=+0.326 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5730.9756 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.311 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.306 (n=220)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.300)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.386 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `2570.3258` → IC=+0.329 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2570.3258 (IC base=+0.300)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.420 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.377)

- **PATRÓN** `py_entrada` > `0.88` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.88 (IC base=+0.377)

- **PATRÓN** `libro_liquidez` > `820.162` → IC=+0.393 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 820.162 (IC base=+0.377)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.412 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.412)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.430 (n=199)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.412)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.423 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.412)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.427 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.412)

- **PATRÓN** `libro_liquidez` > `1921.0334` → IC=+0.424 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1921.0334 (IC base=+0.412)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.411 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.444 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.414)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.426 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.414)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.426 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.414)

- **PATRÓN** `libro_liquidez` > `5399.1782` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5399.1782 (IC base=+0.414)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.412 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.408)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.412 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.408)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.425 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.408)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.413 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.408)

- **PATRÓN** `libro_liquidez` > `1957.89` → IC=+0.439 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1957.89 (IC base=+0.408)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.317 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.274)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.415 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.274)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.288 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `758.501` → IC=+0.284 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 758.501 (IC base=+0.274)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.317 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.274)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.415 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.274)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.288 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `758.501` → IC=+0.284 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 758.501 (IC base=+0.274)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.126 (n=560)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 6.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.9725` → IC=+0.261 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9725 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1542` → IC=+0.235 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1542 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` < `1.024` → IC=+0.239 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.024 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.899` → IC=+0.217 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.899 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` < `0.7215` → IC=+0.233 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7215 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` > `1.1032` → IC=+0.250 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1032 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` < `0.0803` → IC=+0.122 (n=782)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.0803 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.3178` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.3178 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` < `3.1961` → IC=+0.123 (n=868)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 3.1961 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` > `1.4968` → IC=+0.131 (n=867)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4968 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.134 (n=1753)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.4 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` < `0.1289` → IC=+0.145 (n=581)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1289 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.8545` → IC=+0.135 (n=393)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8545 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `1.2608` → IC=+0.143 (n=197)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.2608 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.0812` → IC=+0.253 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0812 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.6694` → IC=+0.227 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6694 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` > `3.1879` → IC=+0.214 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1879 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `140.0` → IC=+0.252 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 140.0 (IC base=+0.048)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.170 (n=195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0071 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.163 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 11.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.349` → IC=+0.343 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.349 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.154 (n=325)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.06 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.319 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.329 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.329 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.297 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.5765` → IC=+0.330 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5765 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.0645` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0645 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.7987` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7987 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.334 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1982.2745` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1982.2745 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.287)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.270 (n=172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.4253` → IC=+0.247 (n=196)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4253 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.264 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.8982` → IC=+0.265 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8982 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.1784` → IC=+0.245 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1784 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` < `1.136` → IC=+0.249 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.136 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.443` → IC=+0.318 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.443 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `0.6608` → IC=+0.235 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6608 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `1.1438` → IC=+0.258 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1438 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.083` → IC=+0.253 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.083 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2912` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2912 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.378` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.378 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.0438` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0438 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `11835.8417` → IC=+0.265 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11835.8417 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.238 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 411.0 (IC base=+0.233)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.171 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0022 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.174 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.148 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.143 (n=334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 18.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.3843` → IC=+0.181 (n=283)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.3843 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.2808` → IC=+0.163 (n=307)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2808 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.029` → IC=+0.243 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.029 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6264` → IC=+0.154 (n=108)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6264 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.2547` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.2547 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.245 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.8414` → IC=+0.196 (n=146)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.8414 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `13676.6856` → IC=+0.188 (n=107)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 13676.6856 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `254.0` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 254.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.182 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0071 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.136 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.912` → IC=+0.287 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.912 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.147 (n=432)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.06 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `1917.67` → IC=+0.146 (n=176)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1917.67 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 23.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.328 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.305 (n=85)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.289 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.285)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.292 (n=262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.5027` → IC=+0.312 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5027 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.013` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.013 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.3362` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3362 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `4.5585` → IC=+0.267 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.5585 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.9495` → IC=+0.286 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9495 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.287 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.285)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `ibs_20min` > `0.882` → IC=-0.189 (n=146)

  - _Acción_: SKIP cuando `ibs_20min` > 0.882
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=441)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.865` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.865 (IC base=+0.002)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.646` → IC=-0.142 (n=219)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.646
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=770)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` < `2.8678` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.8678
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.194 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0059 (IC base=+0.094)

- **PATRÓN** `drift_60min` |x|≤ `0.413` → IC=+0.160 (n=51)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.413 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `23.0` → IC=+0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 23.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.375` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.375 (IC base=+0.094)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` > `0.7414` → IC=-0.141 (n=221)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7414
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=665)

- **FILTRO** `sigma_ewma_delta_pct` > `8.034` → IC=-0.173 (n=105)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.034
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=781)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.08` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 8.08 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.7885` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.7885 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.334` → IC=+0.221 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.334 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.229 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6966 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `1.0971` → IC=+0.233 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0971 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.151 (n=665)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0073 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.9474` → IC=+0.248 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9474 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.322` → IC=+0.253 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.322 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.305` → IC=+0.128 (n=1181)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.305 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` > `1.0271` → IC=+0.166 (n=273)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0271 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.3246` → IC=+0.218 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3246 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` > `3.2058` → IC=+0.170 (n=283)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 3.2058 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.286 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 86.0 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.106` → IC=+0.163 (n=971)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.106 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.6504` → IC=+0.211 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6504 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `0.63` → IC=+0.191 (n=558)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 0.63 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2634` → IC=+0.349 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2634 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `1.6539` → IC=+0.249 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6539 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.238 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.039)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.936` → IC=-0.214 (n=110)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.936
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=552)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.418` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.418 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.0542` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0542 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.317` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.317 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` < `0.0856` → IC=-0.175 (n=121)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0856
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=363)

- **PATRÓN** `volumen_regimen` < `0.5607` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.5607 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` > `1.1074` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1074 (IC base=-0.031)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.292 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0614` → IC=+0.222 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0614 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.263 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.923` → IC=+0.303 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.923 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1444` → IC=+0.187 (n=266)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1444 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.425` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.425 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.0881` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.0881 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `3.9033` → IC=+0.207 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.9033 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.198 (n=405)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.06 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1914.9184` → IC=+0.206 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.9184 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.402 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.372)

- **PATRÓN** `drift_60min` |x|≤ `0.1764` → IC=+0.378 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1764 (IC base=+0.372)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.397 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.372)

- **PATRÓN** `ibs_20min` < `0.3009` → IC=+0.389 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3009 (IC base=+0.372)

- **PATRÓN** `ibs_20min` > `0.0514` → IC=+0.369 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0514 (IC base=+0.372)

- **PATRÓN** `volumen_pendiente_norm` < `0.2282` → IC=+0.403 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2282 (IC base=+0.372)

- **PATRÓN** `volumen_pendiente_norm` > `0.1384` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1384 (IC base=+0.372)

- **PATRÓN** `volumen_spike_ratio` < `2.9764` → IC=+0.444 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9764 (IC base=+0.372)

- **PATRÓN** `libro_liquidez` > `1874.461` → IC=+0.415 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1874.461 (IC base=+0.372)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `dist_vwap_pct` < `0.7343` → IC=-0.227 (n=42)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7343
  - _Potencial_: sin este filtro IC_bueno=+0.333 (n=10)

- **FILTRO** `volumen_regimen` > `0.9592` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9592
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `dist_vwap_pct` < `0.0941` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0941
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `volumen_regimen` > `0.9083` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9083
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=45)

- **FILTRO** `volumen_regimen` < `0.6698` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6698
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=46)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.141 (n=51)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=791)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.48` → IC=-0.153 (n=194)

  - _Acción_: SKIP cuando `ibs_20min` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=195)

- **FILTRO** `dist_vwap_pct` > `0.1326` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1326
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=45)

- **FILTRO** `volumen_regimen` > `1.2618` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.2618
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=41)

- **FILTRO** `volumen_pendiente_norm` < `0.1045` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1045
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `ibs_20min` > `0.7778` → IC=+0.240 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7778 (IC base=-0.006)

- **PATRÓN** `dist_vwap_pct` > `0.1775` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1775 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.1259` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.1259 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2556` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2556 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.7837` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.7837 (IC base=-0.006)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.009` → IC=+0.370 (n=129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.196 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.233 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.9123` → IC=+0.257 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9123 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.2748` → IC=+0.302 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2748 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.118` → IC=+0.257 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.118 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` > `1.0233` → IC=+0.234 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0233 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.1827` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1827 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.9816` → IC=+0.207 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9816 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `2695.6908` → IC=+0.218 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2695.6908 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.362 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.278 (n=264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.262 (n=397)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.3804` → IC=+0.271 (n=396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3804 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.320 (n=203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.2727` → IC=+0.337 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2727 (IC base=+0.260)

- **PATRÓN** `dist_vwap_pct` > `0.5433` → IC=+0.265 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5433 (IC base=+0.260)

- **PATRÓN** `dist_vwap_pct` < `0.7391` → IC=+0.261 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7391 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.479` → IC=+0.274 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.479 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` > `1.0789` → IC=+0.302 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0789 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2467` → IC=+0.385 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2467 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `2.8167` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8167 (IC base=+0.260)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.201 (n=765)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.156 (n=1138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 11.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.9108` → IC=+0.258 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9108 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.8069` → IC=+0.248 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8069 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.347` → IC=+0.287 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.347 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.6367` → IC=+0.166 (n=1037)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6367 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.1052` → IC=+0.183 (n=588)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1052 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.4442` → IC=+0.141 (n=1271)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4442 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.4866` → IC=+0.144 (n=1444)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4866 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.166 (n=1745)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.04 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `3281.7667` → IC=+0.206 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3281.7667 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.207 (n=1485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.2474` → IC=+0.205 (n=1307)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2474 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.3898` → IC=+0.257 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3898 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.4373` → IC=+0.177 (n=1333)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.4373 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.607` → IC=+0.210 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.607 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.27` → IC=+0.194 (n=1493)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 5.27 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.1867` → IC=+0.168 (n=1185)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1867 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` > `0.6787` → IC=+0.174 (n=1058)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6787 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.251` → IC=+0.238 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.251 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.6192` → IC=+0.190 (n=388)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.6192 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.8566` → IC=+0.220 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8566 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.182 (n=391)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 115.0 (IC base=+0.193)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.210 (n=153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.333 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.377` → IC=+0.359 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.377 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1402` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1402 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.4192` → IC=+0.134 (n=260)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4192 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.186 (n=269)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.06 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.302 (n=94)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.316 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.2108` → IC=+0.332 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2108 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.315 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.4177` → IC=+0.323 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4177 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` < `0.0686` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0686 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `1.8747` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8747 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.374 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1966.1335` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1966.1335 (IC base=+0.291)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.235 (n=66)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.218 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0035 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.5283` → IC=+0.245 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5283 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.2332` → IC=+0.252 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2332 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.145` → IC=+0.313 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.145 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `0.9291` → IC=+0.246 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9291 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2949` → IC=+0.274 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2949 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.4313` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4313 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.6559` → IC=+0.207 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6559 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `11116.6074` → IC=+0.246 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11116.6074 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.196 (n=287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.004 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.2033` → IC=+0.209 (n=252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2033 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.193 (n=268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 7.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.3222` → IC=+0.222 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3222 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.1339` → IC=+0.196 (n=291)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1339 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.574` → IC=+0.263 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.574 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.627` → IC=+0.235 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.627 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.0714` → IC=+0.227 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0714 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.808` → IC=+0.230 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.808 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `13319.6098` → IC=+0.173 (n=96)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 13319.6098 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 221.0 (IC base=+0.168)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.198 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0076 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.1433` → IC=+0.157 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1433 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.156 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.212 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.804` → IC=+0.328 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.804 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.2317` → IC=+0.134 (n=249)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.2317 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.0183` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0183 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `3.9092` → IC=+0.138 (n=114)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 3.9092 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.175 (n=244)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.04 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `1970.8484` → IC=+0.160 (n=104)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1970.8484 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.339 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.302)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.304 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.2366` → IC=+0.326 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2366 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.329 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` < `0.3486` → IC=+0.323 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3486 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.578` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.578 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.3308` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3308 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` < `4.3528` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.3528 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.312 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.302)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.258 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0088 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.0915` → IC=+0.297 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0915 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.237 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.223 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.481` → IC=+0.285 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.481 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1224` → IC=+0.243 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1224 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.3604` → IC=+0.236 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3604 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.691` → IC=+0.405 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.691 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6466` → IC=+0.253 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6466 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.1034` → IC=+0.289 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1034 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.4673` → IC=+0.238 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4673 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.6063` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6063 (IC base=+0.225)

- **PATRÓN** `ballena_activa_n` < `243.0` → IC=+0.213 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 243.0 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.205 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.3139` → IC=+0.174 (n=283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3139 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.153 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 18.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.4404` → IC=+0.223 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4404 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.3707` → IC=+0.172 (n=327)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.3707 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.644` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.644 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.1858` → IC=+0.177 (n=283)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1858 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.6089` → IC=+0.155 (n=282)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6089 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.1688` → IC=+0.136 (n=182)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1688 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1088` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1088 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.8878` → IC=+0.186 (n=119)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.8878 (IC base=+0.151)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.4844` → IC=-0.227 (n=97)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4844
  - _Potencial_: sin este filtro IC_bueno=+0.211 (n=292)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.208 (n=142)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.219 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8667 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.724` → IC=+0.256 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.724 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.462` → IC=+0.242 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.462 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2685.4936` → IC=+0.181 (n=142)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2685.4936 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.226 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.215 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.4844` → IC=+0.211 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4844 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.974` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 6.974 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` > `0.8432` → IC=+0.140 (n=195)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8432 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.094` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.094 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `1.502` → IC=+0.127 (n=164)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.502 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2374.302` → IC=+0.189 (n=133)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2374.302 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 32.0 (IC base=+0.101)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.246 (n=230)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.3181` → IC=+0.152 (n=303)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3181 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.244 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.3045` → IC=+0.212 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3045 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.341` → IC=+0.239 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.341 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6079` → IC=+0.167 (n=115)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6079 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.8419` → IC=+0.164 (n=230)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.8419 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1822` → IC=+0.241 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1822 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.68` → IC=+0.169 (n=309)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.68 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.9139` → IC=+0.159 (n=206)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.9139 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2464.8952` → IC=+0.163 (n=345)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2464.8952 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.260 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.286 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.250 (n=126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.2585` → IC=+0.306 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2585 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` < `0.1309` → IC=+0.239 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1309 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.735` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.735 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` > `0.6885` → IC=+0.265 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6885 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.2498` → IC=+0.346 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2498 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `3.0855` → IC=+0.279 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0855 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.180 (n=95)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 30.0 (IC base=+0.231)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.167 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0062 (IC base=+0.072)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.220 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.525` → IC=+0.132 (n=264)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.525 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.5629` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.5629 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.717` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.717 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.1851` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1851 (IC base=+0.072)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 124.0 (IC base=+0.072)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.290 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.2391` → IC=+0.141 (n=157)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.2391 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.883` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.883 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` < `1.7241` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7241 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.056)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.214 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=26)

- **FILTRO** `ibs_20min` < `0.2178` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2178
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.143 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 11.0 (IC base=-0.037)

- **PATRÓN** `ibs_20min` > `0.2178` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.2178 (IC base=-0.037)

- **PATRÓN** `libro_liquidez` > `6332.2628` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 6332.2628 (IC base=-0.037)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.250 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.283 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0923 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.172 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 4.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.219 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.2561` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2561 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.1812` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1812 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.2203` → IC=+0.162 (n=66)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2203 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.889` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.889 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.2387` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.2387 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `0.7034` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7034 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.091` → IC=+0.357 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.091 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.5649` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5649 (IC base=+0.163)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `sigma_h` > `0.0045` → IC=-0.154 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0045
  - _Potencial_: sin este filtro IC_bueno=+0.211 (n=50)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.226 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.231)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.271 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.003 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.1974` → IC=+0.271 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1974 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.342 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.5669` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5669 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` < `0.298` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.298 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.836` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.836 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `0.7015` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7015 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` > `1.1837` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1837 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `2.3331` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3331 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.0232` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0232 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `2693.0092` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2693.0092 (IC base=+0.231)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.352 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.092)

- **PATRÓN** `drift_60min` |x|≤ `0.2707` → IC=+0.186 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.2707 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.232 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.529` → IC=+0.121 (n=56)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.529 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.121` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.121 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `9493.103` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9493.103 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=70)

- **FILTRO** `dist_vwap_pct` > `0.1746` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1746
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=73)

- **FILTRO** `volumen_pendiente_norm` > `0.1087` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1087
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=48)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 1.0 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.98` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 7.98 (IC base=+0.035)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.214 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.781` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.781 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.99` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.99 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.0773` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0773 (IC base=+0.029)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.223 (n=644)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.160 (n=961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.147 (n=718)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.96` → IC=+0.286 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.96 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.3075` → IC=+0.213 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3075 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.049` → IC=+0.263 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.049 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.714` → IC=+0.147 (n=530)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.714 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.0961` → IC=+0.142 (n=546)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0961 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1702` → IC=+0.163 (n=470)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1702 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.8983` → IC=+0.131 (n=1617)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.8983 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.6251` → IC=+0.141 (n=1444)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.6251 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.147 (n=1958)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.04 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2764.1008` → IC=+0.185 (n=874)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2764.1008 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.207 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 168.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.214 (n=1760)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.3422` → IC=+0.202 (n=1759)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3422 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.213 (n=810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` < `0.5337` → IC=+0.256 (n=1759)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5337 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.7203` → IC=+0.176 (n=1395)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.7203 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.143` → IC=+0.227 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.143 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.52` → IC=+0.195 (n=1650)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 2.52 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.6117` → IC=+0.181 (n=427)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6117 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` > `1.2004` → IC=+0.182 (n=426)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.2004 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2382` → IC=+0.241 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2382 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.205 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.130 (n=422)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 55.0 (IC base=+0.192)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.210 (n=184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.158 (n=276)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 11.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.289 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.154` → IC=+0.356 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.154 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2113` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2113 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.159 (n=297)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.06 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.312 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.287 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.2086` → IC=+0.329 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2086 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.300 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.5819` → IC=+0.339 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5819 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.0647` → IC=+0.312 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0647 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.316 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1989.2275` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1989.2275 (IC base=+0.287)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.164 (n=111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0026 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.171 (n=168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0033 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.3307` → IC=+0.224 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3307 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.2065` → IC=+0.241 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2065 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.732` → IC=+0.265 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.732 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6746` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6746 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.9205` → IC=+0.176 (n=168)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.9205 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.1007` → IC=+0.182 (n=193)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1007 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1502` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1502 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.6604` → IC=+0.205 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6604 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.3527` → IC=+0.204 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3527 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `10070.4177` → IC=+0.224 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10070.4177 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.202 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3097` → IC=+0.176 (n=316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3097 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.170 (n=280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.4925` → IC=+0.211 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4925 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.2693` → IC=+0.190 (n=308)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2693 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.611` → IC=+0.246 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.611 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.6202` → IC=+0.213 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6202 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.8408` → IC=+0.179 (n=210)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.8408 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0953` → IC=+0.289 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0953 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.7476` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7476 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `12510.8748` → IC=+0.201 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12510.8748 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `360.0` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 360.0 (IC base=+0.164)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.245 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.717` → IC=+0.247 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.717 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.864` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.864 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` < `0.2327` → IC=+0.168 (n=251)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.2327 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.1733` → IC=+0.149 (n=109)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1733 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `4.0128` → IC=+0.170 (n=113)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 4.0128 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.190 (n=349)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.06 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `1854.4986` → IC=+0.185 (n=214)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1854.4986 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.332 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.273 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.282 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.5575` → IC=+0.340 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5575 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.2282` → IC=+0.224 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2282 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.4009` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4009 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `2.5357` → IC=+0.276 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5357 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.147 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0022 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.171 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.007 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.0729` → IC=+0.171 (n=83)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0729 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.3749` → IC=+0.217 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3749 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.2757` → IC=+0.205 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2757 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.602` → IC=+0.208 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.602 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.7618` → IC=+0.205 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7618 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `1.1336` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1336 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.4306` → IC=+0.231 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4306 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3817.4959` → IC=+0.220 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3817.4959 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `238.0` → IC=+0.256 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 238.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.258 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3707` → IC=+0.147 (n=202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3707 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.127 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.155 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.2508` → IC=+0.223 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2508 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.145` → IC=+0.129 (n=114)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.145 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.6091` → IC=+0.156 (n=213)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.6091 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.785` → IC=+0.267 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.785 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.539` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.539 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.0653` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.0653 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2546` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2546 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `2.1206` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.1206 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.5454` → IC=+0.179 (n=132)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.5454 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `8869.2481` → IC=+0.138 (n=92)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 8869.2481 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=+0.124)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `ibs_20min` > `0.5854` → IC=-0.186 (n=103)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5854
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=311)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.199 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.061)

- **PATRÓN** `ibs_20min` > `0.9375` → IC=+0.241 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9375 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.6498` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6498 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.901` → IC=+0.259 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.901 (IC base=+0.061)

- **PATRÓN** `libro_liquidez` > `2610.6456` → IC=+0.199 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2610.6456 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.243 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.061)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.145 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0073 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1373` → IC=+0.147 (n=137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1373 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.169 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.5854` → IC=+0.200 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5854 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.3719` → IC=+0.142 (n=258)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3719 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.476` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 7.476 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.6196` → IC=+0.141 (n=104)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6196 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` > `1.0614` → IC=+0.129 (n=141)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.0614 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` < `0.1499` → IC=+0.157 (n=176)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.1499 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` > `1.5536` → IC=+0.180 (n=148)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.5536 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `1218.3774` → IC=+0.155 (n=207)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1218.3774 (IC base=+0.103)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.259 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.0893` → IC=+0.193 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0893 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.162 (n=193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 8.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.280 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.2884` → IC=+0.253 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2884 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.835` → IC=+0.249 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.835 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.6001` → IC=+0.186 (n=135)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6001 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.0463` → IC=+0.170 (n=183)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.0463 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2483` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2483 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.635` → IC=+0.168 (n=317)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.635 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=427)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `2464.8952` → IC=+0.164 (n=403)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2464.8952 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.235 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.292 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3909` → IC=+0.233 (n=451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3909 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.272 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.4611` → IC=+0.286 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4611 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.6843` → IC=+0.224 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6843 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.929` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.929 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.8` → IC=+0.222 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.8 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.8813` → IC=+0.243 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8813 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2899` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2899 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.7303` → IC=+0.237 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7303 (IC base=+0.213)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=313)

- **PATRÓN** `dist_vwap_pct` > `0.2171` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.2171 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `7567.9194` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 7567.9194 (IC base=+0.040)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.213 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.2554` → IC=+0.176 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2554 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.196 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 4.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.678` → IC=+0.171 (n=247)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.678 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.4165` → IC=+0.152 (n=251)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.4165 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.471` → IC=+0.146 (n=235)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 5.471 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.1687` → IC=+0.171 (n=217)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.1687 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.0956` → IC=+0.146 (n=210)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0956 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.698` → IC=+0.171 (n=244)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.698 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4141` → IC=+0.141 (n=243)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4141 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=313)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `6608.3768` → IC=+0.194 (n=246)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 6608.3768 (IC base=+0.136)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **FILTRO** `dist_vwap_pct` < `0.5259` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.5259
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.176 (n=137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0037 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0648` → IC=+0.229 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0648 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.284 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.025` → IC=+0.230 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.025 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.3385` → IC=+0.164 (n=147)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.3385 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.805` → IC=+0.169 (n=146)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 9.805 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.2781` → IC=+0.162 (n=137)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2781 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.7036` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.7036 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1578` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1578 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.827` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.827 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.4122` → IC=+0.162 (n=137)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4122 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `9861.9143` → IC=+0.155 (n=137)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 9861.9143 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `696.0` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 696.0 (IC base=+0.147)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.208 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.4762` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.4762 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.1682` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1682 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.19` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 4.19 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.657` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.657 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1138` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1138 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `2.4297` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4297 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `9005.1548` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9005.1548 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.306 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.2126` → IC=+0.300 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2126 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.256 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.612` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.612 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.1184` → IC=+0.280 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1184 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.5036` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5036 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.1217` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1217 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.54` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.54 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.2832` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2832 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1261` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1261 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `2.6912` → IC=+0.269 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6912 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `7397.5021` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7397.5021 (IC base=+0.224)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.01` → IC=-0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **FILTRO** `sigma_ewma_delta_pct` < `1.963` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 1.963
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.149 (n=55)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.219 (n=112)

- **FILTRO** `sigma_h` > `0.0111` → IC=-0.296 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=160)

- **FILTRO** `dist_vwap_pct` > `0.1067` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1067
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `volumen_spike_ratio` < `2.7298` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.7298
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=16)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.180 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0054 (IC base=+0.057)

- **PATRÓN** `drift_60min` |x|≤ `0.1151` → IC=+0.151 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1151 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.379` → IC=+0.213 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.379 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `1.0949` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0949 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.0847` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0847 (IC base=+0.057)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=111)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2013.1835` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2013.1835 (IC base=+0.057)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=42)

- **FILTRO** `sigma_h` > `0.0036` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=36)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.7342` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7342 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.15` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 13.15 (IC base=+0.062)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.326 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=43)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.360 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=23)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.242 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.368 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.1209` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1209 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.41` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.41 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `0.8241` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8241 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `1.0919` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0919 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2340.5972` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2340.5972 (IC base=+0.100)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0165` → IC=-0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0165
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=59)

- **FILTRO** `ibs_20min` > `0.4286` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4286
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `volumen_regimen` > `0.903` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.903
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=-0.020)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=-0.020)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.423 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=58)

- **FILTRO** `dist_vwap_pct` > `0.0767` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0767
  - _Potencial_: sin este filtro IC_bueno=-0.290 (n=79)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

- **FILTRO** `dist_vwap_pct` > `0.3507` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3507
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=80)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `ibs_20min` < `0.5407` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5407
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` < `10.347` → IC=-0.463 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 10.347
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `sigma_h` > `0.0018` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `dist_vwap_pct` > `0.0802` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0802
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `ibs_20min` < `0.6` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `ibs_20min` < `0.7391` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7391
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.5333` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5333
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=101)

- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.144 (n=133)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6429 (IC base=+0.059)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.125 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `ibs_20min` < `0.3927` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3927
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=39)

- **PATRÓN** `ibs_20min` > `0.7184` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7184 (IC base=-0.067)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.3803` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.3803 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.84` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.84 (IC base=+0.085)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.991` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.991 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `2399.5952` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2399.5952 (IC base=+0.159)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.095)

- **PATRÓN** `drift_60min` |x|≤ `0.1849` → IC=+0.159 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1849 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7333 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.03 (IC base=+0.095)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.198 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 11.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.485 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.5 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `2696.6482` → IC=+0.212 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2696.6482 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.129 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 18.0 (IC base=+0.115)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` > 0.505 (IC base=+0.115)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.198 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 11.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.485 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.5 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `2696.6482` → IC=+0.212 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2696.6482 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.129 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 18.0 (IC base=+0.115)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` > 0.505 (IC base=+0.115)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `17.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=90)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=90)

- **FILTRO** `libro_liquidez` < `1978.7004` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 1978.7004
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=80)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=72)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=82)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `libro_liquidez` < `2892.3985` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2892.3985
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M
- **FILTRO** `hora_utc` < `5.0` → IC=-0.173 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=100)

- **FILTRO** `libro_liquidez` < `3728.1259` → IC=-0.184 (n=36)

  - _Acción_: SKIP cuando `libro_liquidez` < 3728.1259
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=111)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.285 (n=63)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=77)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `libro_liquidez` < `13135.9064` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 13135.9064
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=35)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `liq_imbalance_15min` |x|> `1.0` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `liq_imbalance_15min` |x|> 1.0 (IC base=+0.047)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.227 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.047)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `liq_usd_total` < `24810.11` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 24810.11
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9753` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9753
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=66)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=62)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.128 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=42)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=55)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=56)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2159.7894` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 2159.7894
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=65)

- **FILTRO** `drift_20min_pct` |x|> `0.1411` → IC=-0.143 (n=40)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1411
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=80)

- **PATRÓN** `libro_liquidez` > `2159.7894` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2159.7894 (IC base=+0.034)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.1411` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `drift_20min_pct` |x|≤ 0.1411 (IC base=+0.033)

### MOMENTUM_IBS_15M#DOGE#15min
- **FILTRO** `ibs_20min` > `0.9426` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9426
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=91)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=157)

- **PATRÓN** `ibs_20min` > `0.9979` → IC=+0.139 (n=59)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.9979 (IC base=+0.029)

### MOMENTUM_IBS_15M#SOL#15min
- **PATRÓN** `drift_20min_pct` |x|≤ `0.1191` → IC=+0.135 (n=72)

  - _Acción_: Kelly boost +0.68€ cuando `drift_20min_pct` |x|≤ 0.1191 (IC base=+0.057)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.45` → IC=-0.165 (n=338)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=1044)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.238 (n=338)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1093)

- **FILTRO** `ibs_20min` > `0.2759` → IC=-0.224 (n=356)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1075)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.235 (n=47)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=154)

- **FILTRO** `ibs_20min` < `0.8306` → IC=-0.147 (n=100)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8306
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=101)

- **FILTRO** `ibs_20min` > `0.1846` → IC=-0.169 (n=119)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1846
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=120)

- **PATRÓN** `ibs_20min` > `0.8306` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.8306 (IC base=-0.003)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.56` → IC=-0.336 (n=59)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=191)

- **FILTRO** `ibs_20min` > `0.2279` → IC=-0.281 (n=62)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2279
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=188)

- **FILTRO** `ballena_activa_n` > `87.0` → IC=-0.234 (n=62)

  - _Acción_: SKIP cuando `ballena_activa_n` > 87.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=188)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.156 (n=91)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=113)

- **FILTRO** `ibs_20min` < `0.8619` → IC=-0.135 (n=102)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8619
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=102)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.238 (n=59)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=183)

- **FILTRO** `ibs_20min` > `0.7585` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7585
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=182)

- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.153 (n=70)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.9429 (IC base=-0.024)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=200)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.131 (n=82)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=174)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.153 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=176)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.272 (n=55)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=168)

- **FILTRO** `drift_20min_pct` |x|> `0.2833` → IC=-0.202 (n=55)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2833
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=168)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.206 (n=90)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=133)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.200 (n=58)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=180)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=223)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.325 (n=55)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=166)

- **FILTRO** `drift_20min_pct` |x|> `0.2905` → IC=-0.175 (n=75)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2905
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=146)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.325 (n=55)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=166)

- **PATRÓN** `libro_liquidez` > `2476.5327` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2476.5327 (IC base=+0.025)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.300 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=372)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `libro_liquidez` < `2063.3848` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 2063.3848
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` < `1.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

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

- **FILTRO** `drift_7min_pct` |x|> `0.0741` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0741
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=25)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0741` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `drift_7min_pct` |x|≤ 0.0741 (IC base=+0.000)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=74)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.033)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=38)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0611` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `drift_7min_pct` |x|≤ 0.0611 (IC base=+0.029)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33)

- **PATRÓN** `libro_liquidez` > `9401.8411` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 9401.8411 (IC base=+0.041)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `py_entrada` < `0.36` → IC=-0.267 (n=859)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=2611)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.214 (n=864)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2606)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.168 (n=1165)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2305)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.220 (n=1008)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=3157)

- **FILTRO** `ibs_7min` > `0.7009` → IC=-0.155 (n=1041)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7009
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=3124)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.3` → IC=-0.320 (n=120)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=374)

- **FILTRO** `ibs_7min` < `0.9422` → IC=-0.186 (n=326)

  - _Acción_: SKIP cuando `ibs_7min` < 0.9422
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=168)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.215 (n=121)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=373)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.226 (n=184)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=460)

- **FILTRO** `drift_7min_pct` |x|> `0.1303` → IC=-0.182 (n=218)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1303
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=426)

- **FILTRO** `ibs_7min` > `0.8201` → IC=-0.179 (n=160)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8201
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=484)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.138 (n=150)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=494)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.239 (n=178)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=536)

- **FILTRO** `ballena_activa_n` > `93.0` → IC=-0.135 (n=242)

  - _Acción_: SKIP cuando `ballena_activa_n` > 93.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=472)

- **FILTRO** `py_entrada` > `0.51` → IC=-0.178 (n=178)

  - _Acción_: SKIP cuando `py_entrada` > 0.51
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=553)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.181 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=355)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.336 (n=114)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=358)

- **FILTRO** `ibs_7min` < `0.7106` → IC=-0.233 (n=155)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7106
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=317)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.263 (n=116)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=356)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.263 (n=154)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=561)

- **FILTRO** `ibs_7min` > `0.8366` → IC=-0.172 (n=178)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8366
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=537)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.233 (n=148)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=467)

- **FILTRO** `ibs_7min` < `0.788` → IC=-0.177 (n=153)

  - _Acción_: SKIP cuando `ibs_7min` < 0.788
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=462)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.190 (n=153)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=462)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.252 (n=151)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=472)

- **FILTRO** `ibs_7min` > `0.1692` → IC=-0.137 (n=210)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1692
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=413)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.197 (n=153)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=470)

- **FILTRO** `libro_liquidez` < `8732.8793` → IC=-0.132 (n=411)

  - _Acción_: SKIP cuando `libro_liquidez` < 8732.8793
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=212)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.196 (n=159)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=484)

- **FILTRO** `ibs_7min` < `0.7778` → IC=-0.167 (n=160)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7778
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=483)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.211 (n=154)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=489)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.156 (n=190)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=578)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.269 (n=132)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=400)

- **FILTRO** `ibs_7min` < `0.7436` → IC=-0.241 (n=133)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7436
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=399)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.240 (n=129)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=403)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.282 (n=172)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=512)

- **FILTRO** `drift_7min_pct` |x|> `0.1355` → IC=-0.141 (n=341)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1355
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=343)

- **FILTRO** `ibs_7min` > `0.2941` → IC=-0.171 (n=232)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=452)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.145 (n=229)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=455)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=149)

- **FILTRO** `drift_7min_pct` |x|> `0.106` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.106
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=116)

- **FILTRO** `ibs_7min` > `0.0606` → IC=-0.133 (n=58)

  - _Acción_: SKIP cuando `ibs_7min` > 0.0606
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=117)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=319)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=489)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=248)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=435)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.144 (n=209)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.109)

- **PATRÓN** `total_vol_5m` < `381.605` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 381.605 (IC base=+0.109)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4202` → IC=+0.143 (n=26)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.4202 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.104)

- **PATRÓN** `total_vol_5m` < `337.955` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `total_vol_5m` < 337.955 (IC base=+0.104)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.061)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0084` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=65)

- **FILTRO** `T_h` > `87.9756` → IC=-0.365 (n=72)

  - _Acción_: SKIP cuando `T_h` > 87.9756
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=36)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.147 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0039 (IC base=-0.169)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.350 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=19)

- **FILTRO** `T_h` > `111.9936` → IC=-0.455 (n=20)

  - _Acción_: SKIP cuando `T_h` > 111.9936
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=22)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=-0.161)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `95.1632` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `T_h` > 95.1632
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=26)

- **FILTRO** `sigma_h` > `0.0033` → IC=-0.326 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

- **PATRÓN** `pct_vs_K` |x|≤ `1.3968` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.3968 (IC base=-0.116)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` > `0.0029` → IC=-0.326 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0029
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `95.1632` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `T_h` > 95.1632
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `5.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `streak_estiramiento` > `0.4086` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4086
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.49` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=49)

- **FILTRO** `streak_estiramiento` > `0.437` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.437
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

- **FILTRO** `libro_liquidez` < `1786.3532` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 1786.3532
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=43)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.015)

### STREAK_FADE_5M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=128)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.154 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 4.0 (IC base=+0.010)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=37)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=36)

- **FILTRO** `libro_liquidez` < `3627.5123` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 3627.5123
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=39)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=+0.017)

- **PATRÓN** `libro_liquidez` > `3627.5123` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3627.5123 (IC base=+0.017)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=44)

- **FILTRO** `streak_estiramiento` > `0.644` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.644
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=50)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 8.0 (IC base=+0.065)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=81)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=45)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=75)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.123 (n=59)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.505 (IC base=+0.069)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.134 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=110)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.122 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 16.0 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 25.0 (IC base=+0.067)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=897)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=518)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=526)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.151 (n=150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0035 (IC base=+0.111)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.133 (n=227)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0048 (IC base=+0.111)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0656` → IC=+0.135 (n=340)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0656 (IC base=+0.111)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.193 (n=350)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.97€ cuando `ibs_15` > 0.5 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.3538` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.3538 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.501` → IC=+0.244 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.501 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `5616.6972` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 5616.6972 (IC base=+0.111)

### UPDOWN_GBM#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.01` → IC=-0.127 (n=199)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=106)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1457` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1457
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **FILTRO** `ibs_15` < `0.1327` → IC=-0.231 (n=76)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1327
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=229)

- **FILTRO** `sigma_ewma_delta_pct` > `6.817` → IC=-0.186 (n=49)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.817
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=256)

### UPDOWN_GBM#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=176)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0397` → IC=-0.227 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0397
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=39)

- **FILTRO** `hora_utc` < `19.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **PATRÓN** `dist_vwap_pct` < `0.16` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.16 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.236` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 17.236 (IC base=+0.037)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.03 (IC base=+0.037)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.004` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=37)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=40)

- **FILTRO** `ibs_15` < `0.3141` → IC=-0.250 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.3141
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=37)

- **FILTRO** `dist_vwap_pct` < `0.1982` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1982
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=34)

- **FILTRO** `libro_liquidez` < `14245.6725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 14245.6725
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=28)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.155 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0032 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.167 (n=76)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0021 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.193` → IC=+0.167 (n=85)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.193 (IC base=+0.149)

- **PATRÓN** `drift_15min` |x|≤ `0.6592` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.6592 (IC base=+0.149)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0878` → IC=+0.167 (n=76)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.0878 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.162 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 13.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.8877` → IC=+0.276 (n=56)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8877 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.367` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.367 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `24.523` → IC=+0.152 (n=90)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 24.523 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11289.7522` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11289.7522 (IC base=+0.149)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2056` → IC=-0.204 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2056
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.415` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 10.415 (IC base=+0.042)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=56)

- **FILTRO** `ibs_15` < `0.6275` → IC=-0.200 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6275
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=55)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.11` → IC=+0.167 (n=31)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.83€ cuando `pct_spot_vs_ref` |x|≤ 0.11 (IC base=+0.022)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.5659` → IC=-0.250 (n=34)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5659
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=70)

- **PATRÓN** `drift_60min` |x|≤ `0.0603` → IC=+0.122 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.0603 (IC base=+0.104)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1873` → IC=+0.237 (n=36)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1873 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.132 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 12.0 (IC base=+0.104)

- **PATRÓN** `ibs_15` > `0.5659` → IC=+0.278 (n=70)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5659 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.0929 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8808.1502` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 8808.1502 (IC base=+0.104)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `ibs_15` < `0.0049` → IC=-0.206 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=48)

- **FILTRO** `dist_vwap_pct` > `0.1641` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1641
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=48)

- **FILTRO** `sigma_ewma_delta_pct` > `5.384` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.384
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=38)

- **FILTRO** `drift_15min` |x|> `0.589` → IC=-0.194 (n=47)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.589
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=144)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=147)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `libro_spread` > `0.03` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=+0.185 (n=52)

- **PATRÓN** `delta_ratio_macro` |x|> `0.175` → IC=+0.167 (n=37)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.175 (IC base=+0.060)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.03 (IC base=+0.060)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=30)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.250 (n=30)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.764` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.764 (IC base=+0.041)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `ibs_15` < `0.1667` → IC=-0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1667
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

- **FILTRO** `sigma_ewma_delta_pct` < `2.288` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 2.288
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0058` → IC=-0.133 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.265 (n=15)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.011)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.163 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.005 (IC base=+0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0626` → IC=+0.133 (n=96)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0626 (IC base=+0.085)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.182 (n=86)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.55 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.4287` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4287 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.54` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.54 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `2507.0533` → IC=+0.136 (n=86)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2507.0533 (IC base=+0.085)

- **PATRÓN** `ibs_15` < `0.1667` → IC=+0.163 (n=99)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` < 0.1667 (IC base=+0.033)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2` → IC=+0.272 (n=90)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2 (IC base=+0.275)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.287 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0023 (IC base=+0.275)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.300 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.1981` → IC=+0.281 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1981 (IC base=+0.275)

- **PATRÓN** `drift_15min` |x|≤ `0.4139` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4139 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.279 (n=102)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.292 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.337 (n=102)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.3696` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3696 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.963` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.963 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `3288.4647` → IC=+0.298 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3288.4647 (IC base=+0.275)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1934` → IC=+0.293 (n=56)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1934 (IC base=+0.250)

- **PATRÓN** `sigma_h` < `0.002` → IC=+0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.002 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.272 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.250)

- **PATRÓN** `drift_15min` |x|≤ `0.411` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.411 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.250 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.250)

- **PATRÓN** `ibs_15` < `0.9942` → IC=+0.250 (n=62)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.9942 (IC base=+0.250)

- **PATRÓN** `ibs_15` > `0.7363` → IC=+0.281 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7363 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` > `0.3665` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3665 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.438` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.438 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` < `15.813` → IC=+0.264 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 15.813 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `6833.6785` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6833.6785 (IC base=+0.250)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.333 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.304)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.304)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.350 (n=18)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.304)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.397 (n=27)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.304)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.333 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.304)

- **PATRÓN** `ibs_15` > `0.785` → IC=+0.423 (n=37)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.785 (IC base=+0.304)

- **PATRÓN** `dist_vwap_pct` > `0.4172` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4172 (IC base=+0.304)

- **PATRÓN** `dist_vwap_pct` < `0.2769` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2769 (IC base=+0.304)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.304)

- **PATRÓN** `libro_liquidez` > `3078.3929` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3078.3929 (IC base=+0.304)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `ibs_15` < `0.3587` → IC=-0.327 (n=73)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.3587
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=221)

- **FILTRO** `sigma_h` > `0.0088` → IC=-0.177 (n=435)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=1307)

- **FILTRO** `ibs_15` > `0.531` → IC=-0.278 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.531
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=52)

- **FILTRO** `sigma_ewma_delta_pct` > `13.453` → IC=-0.200 (n=318)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.453
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=1424)

- **PATRÓN** `ibs_15` > `0.3587` → IC=+0.150 (n=221)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` > 0.3587 (IC base=-0.035)

- **PATRÓN** `ibs_15` < `0.531` → IC=+0.278 (n=52)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.531 (IC base=-0.092)

- **PATRÓN** `dist_vwap_pct` < `0.1453` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1453 (IC base=-0.092)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0061` → IC=-0.237 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=294)

- **FILTRO** `drift_15min` |x|> `0.7549` → IC=-0.207 (n=97)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7549
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=294)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.219 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=304)

- **FILTRO** `sigma_ewma_delta_pct` > `20.323` → IC=-0.238 (n=82)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.323
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=309)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6235` → IC=-0.321 (n=54)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6235
  - _Potencial_: sin este filtro IC_bueno=+0.268 (n=54)

- **PATRÓN** `ibs_15` > `0.6235` → IC=+0.268 (n=54)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6235 (IC base=-0.027)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0954` → IC=+0.204 (n=25)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.0954 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.186 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0039 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.2431` → IC=+0.186 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.2431 (IC base=+0.167)

- **PATRÓN** `drift_15min` |x|≤ `0.6645` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.6645 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.194 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.186 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 14.0 (IC base=+0.167)

- **PATRÓN** `ibs_15` < `0.428` → IC=+0.329 (n=33)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.428 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.899` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 7.899 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.182` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 12.182 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3807.5396` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3807.5396 (IC base=+0.167)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0073` → IC=-0.238 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0073
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=124)

- **FILTRO** `sigma_h` > `0.0078` → IC=-0.148 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=406)

- **FILTRO** `sigma_ewma_delta_pct` > `12.12` → IC=-0.209 (n=101)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.12
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=513)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.666` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.666 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` < `0.0049` → IC=-0.130 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=135)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.147 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=62)

- **FILTRO** `libro_liquidez` < `2506.382` → IC=-0.196 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 2506.382
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=135)

- **FILTRO** `sigma_h` > `0.0082` → IC=-0.186 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=373)

- **FILTRO** `drift_60min` |x|> `0.4546` → IC=-0.185 (n=141)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.4546
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=424)

- **FILTRO** `drift_15min` |x|> `0.855` → IC=-0.157 (n=141)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=424)

- **FILTRO** `sigma_ewma_delta_pct` > `14.667` → IC=-0.257 (n=68)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.667
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=497)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.404 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.1853` → IC=+0.303 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1853 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1863` → IC=+0.343 (n=68)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1863 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2966` → IC=+0.405 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2966 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.333 (n=136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.9701` → IC=+0.371 (n=68)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9701 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.5344` → IC=+0.405 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5344 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` < `0.0845` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0845 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.88` → IC=+0.312 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.88 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.293 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `11189.3992` → IC=+0.327 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11189.3992 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `200.0` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 200.0 (IC base=+0.296)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2038` → IC=+0.289 (n=88)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2038 (IC base=+0.271)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.271 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.306 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0037 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.1837` → IC=+0.311 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1837 (IC base=+0.271)

- **PATRÓN** `drift_15min` |x|≤ `0.6237` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6237 (IC base=+0.271)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.275 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.312 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.271)

- **PATRÓN** `ibs_15` > `0.8845` → IC=+0.312 (n=78)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8845 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.3854` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3854 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` < `0.1026` → IC=+0.304 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1026 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `27.622` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 27.622 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.644` → IC=+0.276 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.644 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `10246.118` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10246.118 (IC base=+0.271)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.364 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.324)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0673` → IC=+0.362 (n=56)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0673 (IC base=+0.324)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.370 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.324)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.333 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.324)

- **PATRÓN** `ibs_15` > `0.8774` → IC=+0.345 (n=56)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8774 (IC base=+0.324)

- **PATRÓN** `dist_vwap_pct` > `0.5578` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5578 (IC base=+0.324)

- **PATRÓN** `dist_vwap_pct` < `0.0758` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0758 (IC base=+0.324)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.173` → IC=+0.351 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.173 (IC base=+0.324)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.324)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0492` → IC=-0.167 (n=22)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0492
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `sigma_h` > `0.0036` → IC=-0.222 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0036
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `drift_60min` |x|> `0.1447` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1447
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `drift_15min` |x|> `0.3418` → IC=-0.167 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3418
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.147 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=251)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1055` → IC=-0.289 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1055
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.237 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.278 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `sigma_h` > `0.0045` → IC=-0.289 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0045
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `63.9936` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9936 (IC base=+0.062)

- **PATRÓN** `ratio` < `0.9702` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9702 (IC base=+0.062)

- **PATRÓN** `T_h` > `146.1118` → IC=+0.452 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.348)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0126 (IC base=+0.348)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `87.9997` → IC=+0.339 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9997 (IC base=+0.266)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.266)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `82.5234` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 82.5234 (IC base=+0.092)

- **PATRÓN** `T_h` < `124.962` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 124.962 (IC base=+0.309)

- **PATRÓN** `T_h` > `111.9838` → IC=+0.311 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.309)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.422)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0058 (IC=+0.265 n=15). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.111 a +0.193 en UPDOWN_GBM#15min (n=350). Ya aplicado como kelly_boost=+0.97€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8877 sube el IC de +0.149 a +0.276 en UPDOWN_GBM#BTC#15min (n=56). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5659 sube el IC de +0.104 a +0.278 en UPDOWN_GBM#ETH#15min (n=70). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.041 a +0.250 en UPDOWN_GBM#SOL#15min (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.085 a +0.182 en UPDOWN_GBM#XRP#15min (n=86). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1667 sube el IC de +0.033 a +0.163 en UPDOWN_GBM#XRP#15min (n=99). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.3587 sube el IC de -0.035 a +0.150 en UPDOWN_GBM_15M_TARDIO (n=221). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.531 sube el IC de -0.092 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=52). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6235 sube el IC de -0.027 a +0.268 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=54). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.428 sube el IC de +0.167 a +0.329 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=33). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9701 sube el IC de +0.296 a +0.371 en UPDOWN_GBM_IBS_ALTO (n=68). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8845 sube el IC de +0.271 a +0.312 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=78). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8774 sube el IC de +0.324 a +0.345 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=56). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.275 a +0.337 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=102). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS < 0.9942 sube el IC de +0.250 a +0.250 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.7363 sube el IC de +0.250 a +0.281 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.785 sube el IC de +0.304 a +0.423 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=37). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#DOGE#5min` — IC=+0.106 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#DOGE` — IC=+0.106 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#SOL#5min` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#SOL` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 534 | +0.067 | +43.16€ | 3 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 534 | +0.067 | +43.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 290 | +0.082 | +32.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 290 | +0.082 | +32.15€ | 2 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 215 | +0.030 | +0.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 215 | +0.030 | +0.07€ | 6 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 4773 | -0.105 | -569.44€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 556 | -0.075 | -93.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 4217 | -0.108 | -475.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 584 | -0.126 | -84.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 584 | -0.126 | -84.58€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 556 | -0.075 | -93.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 556 | -0.075 | -93.86€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 359 | -0.137 | -154.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 359 | -0.137 | -154.67€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 1389 | -0.008 | +26.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 1389 | -0.008 | +26.51€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 1160 | -0.192 | -224.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 1160 | -0.192 | -224.05€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 20486 | +0.112 | -1466.50€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 4233 | +0.185 | -149.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 106 | -0.102 | -48.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 13339 | +0.087 | -1264.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2808 | +0.128 | -3.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 2247 | +0.047 | -458.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 16 | -0.089 | -1.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 2226 | +0.050 | -450.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 4422 | +0.137 | -72.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1172 | +0.196 | -60.88€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 2218 | +0.108 | -61.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 990 | +0.141 | +72.58€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 2250 | +0.063 | -368.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 15 | +0.022 | -2.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 2234 | +0.064 | -364.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 4770 | +0.126 | -81.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1559 | +0.169 | -4.98€ | 0 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 2218 | +0.105 | -57.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 981 | +0.109 | -10.14€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 4552 | +0.126 | -361.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1457 | +0.200 | -78.37€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 45 | +0.011 | -8.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 2213 | +0.077 | -209.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 837 | +0.134 | -65.57€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 2245 | +0.115 | -123.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 14 | +0.000 | -0.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 2230 | +0.116 | -120.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4351 | +0.171 | -357.27€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 4351 | +0.171 | -357.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1093 | +0.165 | -124.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1093 | +0.165 | -124.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 89 | -0.104 | -0.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 89 | -0.104 | -0.35€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1085 | +0.159 | -134.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1085 | +0.159 | -134.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 973 | +0.225 | -36.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 973 | +0.225 | -36.06€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1032 | +0.190 | -75.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1032 | +0.190 | -75.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 222 | +0.429 | -5.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 222 | +0.429 | -5.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 81 | +0.428 | -1.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 81 | +0.428 | -1.09€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 86 | +0.409 | -4.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 86 | +0.409 | -4.43€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 52 | +0.426 | -0.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 52 | +0.426 | -0.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 9527 | +0.195 | -832.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 9527 | +0.195 | -832.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1778 | +0.116 | -359.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1778 | +0.116 | -359.99€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 1474 | +0.240 | -29.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 1474 | +0.240 | -29.89€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 1663 | +0.157 | -236.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 1663 | +0.157 | -236.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1510 | +0.241 | -29.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1510 | +0.241 | -29.73€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 1503 | +0.237 | -40.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 1503 | +0.237 | -40.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1599 | +0.198 | -136.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1599 | +0.198 | -136.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3412 | +0.131 | +71.19€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 3412 | +0.131 | +71.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 1694 | +0.144 | +74.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 1694 | +0.144 | +74.55€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 1718 | +0.118 | -3.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 1718 | +0.118 | -3.36€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 632 | +0.301 | +6.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 632 | +0.301 | +6.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 268 | +0.278 | -7.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 268 | +0.278 | -7.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 293 | +0.300 | +6.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 293 | +0.300 | +6.12€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 71 | +0.377 | +7.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 71 | +0.377 | +7.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 261 | +0.412 | -11.14€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 261 | +0.412 | -11.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 114 | +0.414 | -4.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 114 | +0.414 | -4.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 118 | +0.408 | -7.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 118 | +0.408 | -7.52€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 29 | +0.371 | +0.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 29 | +0.371 | +0.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 68 | +0.171 | +7.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 21 | +0.239 | +5.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 47 | +0.133 | +2.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 55 | +0.149 | +4.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 8 | +0.080 | +1.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 47 | +0.133 | +2.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 9 | +0.102 | +2.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 9 | +0.102 | +2.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 1846 | +0.105 | -60.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 188 | +0.032 | -18.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 1658 | +0.114 | -41.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 1268 | +0.095 | -48.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 188 | +0.032 | -18.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 1080 | +0.106 | -29.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 578 | +0.128 | -12.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 578 | +0.128 | -12.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 312 | +0.274 | -24.55€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 312 | +0.274 | -24.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 312 | +0.274 | -24.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 312 | +0.274 | -24.55€ | 0 | 4 |
| ✅ GBM_LATE_15M | 5575 | +0.064 | +1893.42€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 5575 | +0.064 | +1893.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 843 | +0.176 | +534.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 843 | +0.176 | +534.73€ | 0 | 17 |
| ✅ GBM_LATE_15M#BTC | 688 | +0.174 | +376.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 688 | +0.174 | +376.11€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 853 | +0.191 | +587.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 853 | +0.191 | +587.35€ | 0 | 18 |
| ✅ GBM_LATE_15M#ETH | 816 | -0.039 | +15.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 816 | -0.039 | +15.41€ | 1 | 1 |
| ✅ GBM_LATE_15M#SOL | 1056 | -0.024 | +160.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1056 | -0.024 | +160.49€ | 4 | 4 |
| ✅ GBM_LATE_15M#XRP | 1319 | -0.015 | +219.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1319 | -0.015 | +219.32€ | 2 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 6528 | +0.044 | +2437.94€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 6528 | +0.044 | +2437.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1126 | -0.028 | +510.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1126 | -0.028 | +510.46€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1341 | -0.032 | +140.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1341 | -0.032 | +140.39€ | 1 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 717 | +0.241 | +658.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 717 | +0.241 | +658.57€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1148 | -0.038 | +21.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1148 | -0.038 | +21.20€ | 6 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1156 | -0.001 | +218.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1156 | -0.001 | +218.61€ | 4 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1040 | +0.224 | +888.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1040 | +0.224 | +888.72€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 4225 | +0.173 | +2870.03€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 4225 | +0.173 | +2870.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 634 | +0.193 | +466.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 634 | +0.193 | +466.11€ | 0 | 16 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 644 | +0.181 | +429.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 644 | +0.181 | +429.04€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 630 | +0.201 | +486.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 630 | +0.201 | +486.64€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 621 | +0.181 | +424.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 621 | +0.181 | +424.31€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 804 | +0.098 | +390.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 804 | +0.098 | +390.50€ | 1 | 16 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 892 | +0.191 | +673.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 892 | +0.191 | +673.43€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 664 | +0.065 | +95.74€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 664 | +0.065 | +95.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 133 | +0.085 | +30.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 133 | +0.085 | +30.00€ | 2 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 139 | +0.160 | +42.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 139 | +0.160 | +42.07€ | 1 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 243 | +0.002 | +10.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 243 | +0.002 | +10.10€ | 3 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 148 | +0.060 | +14.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 148 | +0.060 | +14.84€ | 0 | 5 |
| ✅ GBM_LATE_15M_TARDIO | 4913 | +0.164 | +3141.18€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#15min | 4913 | +0.164 | +3141.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 807 | +0.182 | +553.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 807 | +0.182 | +553.90€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 755 | +0.159 | +449.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 755 | +0.159 | +449.75€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 798 | +0.216 | +655.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 798 | +0.216 | +655.60€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 600 | +0.135 | +303.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 600 | +0.135 | +303.97€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 815 | +0.083 | +364.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 815 | +0.083 | +364.00€ | 1 | 17 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1138 | +0.188 | +813.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1138 | +0.188 | +813.96€ | 0 | 24 |
| ✅ GBM_LATE_5M | 478 | +0.106 | +165.18€ | 1 | 15 |
| ✅ GBM_LATE_5M#5min | 478 | +0.106 | +165.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 208 | +0.129 | +95.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 208 | +0.129 | +95.56€ | 2 | 14 |
| ✅ GBM_LATE_5M#DOGE | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 128 | +0.192 | +71.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 128 | +0.192 | +71.43€ | 0 | 21 |
| ✅ GBM_LATE_5M#SOL | 55 | -0.044 | +0.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 55 | -0.044 | +0.89€ | 2 | 0 |
| ✅ GBM_LATE_5M#XRP | 74 | +0.053 | +1.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 74 | +0.053 | +1.71€ | 0 | 0 |
| ✅ GBM_LATE_60M | 501 | -0.045 | +74.00€ | 4 | 8 |
| ✅ GBM_LATE_60M#60min | 501 | -0.045 | +74.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 173 | -0.003 | +5.67€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 173 | -0.003 | +5.67€ | 3 | 3 |
| ✅ GBM_LATE_60M#ETH | 177 | -0.020 | +44.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 177 | -0.020 | +44.02€ | 2 | 8 |
| ✅ GBM_LATE_60M#SOL | 151 | -0.121 | +24.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 151 | -0.121 | +24.30€ | 3 | 2 |
| 🚫 GBM_LATE_60M_FADE | 193 | -0.305 | -34.48€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 193 | -0.305 | -34.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 76 | -0.256 | -7.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 76 | -0.256 | -7.36€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 52 | -0.296 | -8.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 52 | -0.296 | -8.07€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 311 | +0.040 | +5.51€ | 1 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 311 | +0.040 | +5.51€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 121 | +0.012 | +3.09€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 121 | +0.012 | +3.09€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 74 | +0.092 | +5.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 74 | +0.092 | +5.73€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 116 | +0.034 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 116 | +0.034 | -3.31€ | 1 | 5 |
| ✅ LEADLAG_BTC_XRP_15M | 151 | +0.141 | +49.63€ | 0 | 6 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 151 | +0.141 | +49.63€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 151 | +0.141 | +49.63€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 151 | +0.141 | +49.63€ | 0 | 6 |
| ✅ LIQUIDACIONES_15M | 208 | -0.110 | -28.93€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 208 | -0.110 | -28.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 51 | -0.104 | -7.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 51 | -0.104 | -7.11€ | 1 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 44 | -0.043 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 44 | -0.043 | -3.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 40 | -0.024 | -2.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 40 | -0.024 | -2.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 256 | -0.136 | -39.76€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 256 | -0.136 | -39.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 9 | -0.061 | -1.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 9 | -0.061 | -1.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 61 | -0.167 | -11.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 61 | -0.167 | -11.42€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 14 | -0.131 | -3.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 14 | -0.131 | -3.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 80 | -0.073 | -8.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 80 | -0.073 | -8.63€ | 2 | 2 |
| ✅ LIQUIDACIONES_5M#SOL | 60 | -0.129 | -8.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 60 | -0.129 | -8.58€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 32 | -0.176 | -6.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 32 | -0.176 | -6.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 336 | +0.003 | -3.72€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 336 | +0.003 | -3.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 108 | -0.009 | -7.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 108 | -0.009 | -7.43€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 109 | -0.022 | -2.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 109 | -0.022 | -2.44€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 119 | +0.037 | +6.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 119 | +0.037 | +6.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 1951 | +0.007 | -17.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 1951 | +0.007 | -17.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 206 | +0.034 | +17.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 206 | +0.034 | +17.76€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M#BTC | 347 | +0.027 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 347 | +0.027 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 276 | -0.011 | -18.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 276 | -0.011 | -18.58€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 376 | +0.013 | +18.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 376 | +0.013 | +18.50€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M#SOL | 373 | +0.012 | -13.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 373 | +0.012 | -13.83€ | 0 | 1 |
| ✅ MOMENTUM_IBS_15M#XRP | 373 | -0.023 | -21.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 373 | -0.023 | -21.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 2813 | -0.030 | +88.27€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 2813 | -0.030 | +88.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 440 | -0.032 | +56.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 440 | -0.032 | +56.60€ | 3 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 509 | -0.034 | -21.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 509 | -0.034 | -21.25€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 446 | -0.029 | +52.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 446 | -0.029 | +52.63€ | 4 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 503 | -0.013 | +4.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 503 | -0.013 | +4.69€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 456 | -0.046 | +6.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 456 | -0.046 | +6.75€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 459 | -0.025 | -11.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 459 | -0.025 | -11.14€ | 5 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE | 552 | -0.060 | -42.37€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 552 | -0.060 | -42.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 66 | -0.059 | -4.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 66 | -0.059 | -4.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 34 | -0.083 | -3.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 34 | -0.083 | -3.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 108 | -0.118 | -14.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 108 | -0.118 | -14.05€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 139 | -0.032 | -7.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 139 | -0.032 | -7.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 1085 | +0.001 | -1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 1085 | +0.001 | -1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 119 | -0.029 | -0.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 119 | -0.029 | -0.78€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 171 | +0.009 | -2.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 171 | +0.009 | -2.20€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 123 | +0.012 | +0.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 123 | +0.012 | +0.52€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#ETH | 194 | +0.005 | +5.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 194 | +0.005 | +5.37€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#SOL | 312 | +0.003 | +1.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 312 | +0.003 | +1.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 166 | -0.006 | -5.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 166 | -0.006 | -5.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 7635 | -0.066 | +233.52€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 7635 | -0.066 | +233.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 1138 | -0.101 | +99.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 1138 | -0.101 | +99.15€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 1445 | -0.053 | +60.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 1445 | -0.053 | +60.07€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 1187 | -0.064 | +55.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 1187 | -0.064 | +55.20€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 1238 | -0.084 | -60.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 1238 | -0.084 | -60.16€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 1411 | -0.043 | +26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 1411 | -0.043 | +26.02€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 1216 | -0.060 | +53.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 1216 | -0.060 | +53.25€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 5491 | -0.010 | -104.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 5491 | -0.010 | -104.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 868 | +0.016 | +2.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 868 | +0.016 | +2.60€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1000 | -0.019 | -29.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1000 | -0.019 | -29.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1126 | -0.006 | -17.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1126 | -0.006 | -17.52€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 725 | -0.020 | -23.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 725 | -0.020 | -23.89€ | 2 | 0 |
| ✅ ORDER_FLOW_5M | 315 | +0.074 | +50.69€ | 1 | 2 |
| ✅ ORDER_FLOW_5M#5min | 179 | +0.086 | +38.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 51 | +0.104 | +17.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 51 | +0.104 | +17.82€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 31 | +0.106 | +8.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 31 | +0.106 | +8.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 21 | +0.022 | +1.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 21 | +0.022 | +1.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 37 | +0.090 | +5.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 37 | +0.090 | +5.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 39 | +0.061 | +4.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 39 | +0.061 | +4.65€ | 0 | 1 |
| ✅ PRICE_TARGET_GBM | 232 | -0.154 | -16.88€ | 2 | 1 |
| 🚫 PRICE_TARGET_GBM#BTC | 99 | -0.213 | -27.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 86 | -0.227 | -24.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 13 | -0.065 | -2.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 91 | -0.145 | -3.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 76 | -0.154 | -5.11€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 15 | -0.066 | +1.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 42 | -0.023 | +14.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 37 | +0.013 | +15.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 199 | -0.157 | -13.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 33 | -0.129 | -2.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 138 | -0.214 | -1.54€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 59 | -0.156 | +2.56€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 57 | -0.144 | +3.58€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 59 | -0.238 | -7.59€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 57 | -0.229 | -6.57€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 20 | -0.273 | +3.48€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 19 | -0.249 | +3.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 133 | -0.204 | +1.01€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 5 | -0.089 | -2.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 49 | +0.245 | +6.70€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 17 | +0.380 | +8.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 17 | +0.380 | +8.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 49 | +0.245 | +6.70€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 96 | -0.051 | -10.82€ | 6 | 1 |
| ✅ STREAK_FADE_15M#15min | 96 | -0.051 | -10.82€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 43 | +0.011 | -2.26€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 43 | +0.011 | -2.26€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 6 | -0.037 | -1.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 6 | -0.037 | -1.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 9 | +0.021 | -0.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 9 | +0.021 | -0.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 38 | -0.125 | -7.22€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 38 | -0.125 | -7.22€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 557 | -0.001 | -17.09€ | 1 | 1 |
| ✅ STREAK_FADE_5M#5min | 557 | -0.001 | -17.09€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 188 | +0.021 | +0.37€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 188 | +0.021 | +0.37€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 176 | +0.006 | -4.09€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 176 | +0.006 | -4.09€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 83 | -0.018 | -6.00€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 83 | -0.018 | -6.00€ | 3 | 2 |
| ✅ STREAK_FADE_5M#XRP | 110 | -0.036 | -7.37€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 110 | -0.036 | -7.37€ | 3 | 1 |
| ✅ STREAK_FADE_60M | 18 | -0.045 | -1.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 18 | -0.045 | -1.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 10 | -0.083 | -2.14€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 10 | -0.083 | -2.14€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 8 | +0.040 | +0.87€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 8 | +0.040 | +0.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 1021 | +0.014 | -0.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 1021 | +0.014 | -0.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 352 | +0.017 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 352 | +0.017 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 172 | -0.029 | -6.99€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 172 | -0.029 | -6.99€ | 3 | 0 |
| ✅ STREAK_MOM_5M#SOL | 308 | +0.023 | +2.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 308 | +0.023 | +2.03€ | 1 | 1 |
| ✅ STREAK_MOM_5M#XRP | 189 | +0.034 | +4.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 189 | +0.034 | +4.23€ | 2 | 2 |
| ✅ STRUCT_NO_15M | 2382 | +0.005 | -28.34€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 2382 | +0.005 | -28.34€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 916 | +0.001 | -15.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 916 | +0.001 | -15.65€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 916 | +0.009 | -8.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 916 | +0.009 | -8.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 550 | +0.007 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 550 | +0.007 | -4.68€ | 2 | 0 |
| ✅ UPDOWN_GBM | 3630 | +0.011 | +137.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1515 | +0.050 | +161.03€ | 0 | 7 |
| ✅ UPDOWN_GBM#240min | 166 | +0.018 | +1.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 1605 | -0.019 | -34.44€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 297 | +0.008 | +9.31€ | 3 | 3 |
| ✅ UPDOWN_GBM#BNB | 159 | +0.071 | +24.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 147 | +0.097 | +27.92€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 713 | +0.032 | +52.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 167 | +0.080 | +16.11€ | 5 | 13 |
| ✅ UPDOWN_GBM#BTC#240min | 49 | +0.088 | +6.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 380 | +0.024 | +28.44€ | 1 | 1 |
| ✅ UPDOWN_GBM#BTC#60min | 99 | -0.015 | -0.19€ | 2 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 427 | +0.018 | +10.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 90 | +0.098 | +21.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 335 | -0.007 | -12.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 814 | +0.026 | +38.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 372 | +0.059 | +36.38€ | 1 | 7 |
| ✅ UPDOWN_GBM#ETH#240min | 50 | +0.058 | +2.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 254 | -0.023 | -10.05€ | 5 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 123 | +0.044 | +10.09€ | 1 | 2 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 799 | -0.021 | -22.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 322 | -0.012 | -10.51€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 39 | -0.037 | -3.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 351 | -0.018 | -7.95€ | 2 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 75 | -0.019 | -0.59€ | 1 | 1 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 716 | -0.007 | +35.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 417 | +0.049 | +69.30€ | 0 | 8 |
| ✅ UPDOWN_GBM#XRP#240min | 23 | -0.140 | -3.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 276 | -0.079 | -30.11€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 136 | +0.275 | +6.70€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 136 | +0.275 | +6.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 82 | +0.250 | -2.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 82 | +0.250 | -2.30€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 54 | +0.304 | +9.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 54 | +0.304 | +9.00€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 2432 | -0.076 | +413.93€ | 4 | 3 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 2432 | -0.076 | +413.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 202 | -0.098 | +93.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 202 | -0.098 | +93.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 490 | -0.152 | -34.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 490 | -0.152 | -34.20€ | 4 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 61 | +0.024 | +4.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 61 | +0.024 | +4.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 157 | +0.035 | +37.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 157 | +0.035 | +37.15€ | 1 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 778 | -0.054 | +198.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 778 | -0.054 | +198.16€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 744 | -0.074 | +114.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 744 | -0.074 | +114.27€ | 7 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 16 | -0.044 | -1.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 16 | -0.044 | -1.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 16 | -0.044 | -1.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 16 | -0.044 | -1.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 199 | +0.296 | +146.91€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 199 | +0.296 | +146.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 116 | +0.271 | +71.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 116 | +0.271 | +71.74€ | 0 | 13 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 83 | +0.324 | +75.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 83 | +0.324 | +75.17€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 368 | -0.062 | -28.63€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 368 | -0.062 | -28.63€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 233 | -0.006 | -11.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 233 | -0.006 | -11.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 23 | +0.020 | +3.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 23 | +0.020 | +3.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 26 | -0.179 | -5.17€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 26 | -0.179 | -5.17€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 29 | -0.177 | -4.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 29 | -0.177 | -4.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 28 | -0.200 | -4.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 28 | -0.200 | -4.70€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 993 | +0.287 | +396.85€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 295 | +0.200 | +2.11€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 312 | +0.258 | +69.34€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 386 | +0.374 | +325.39€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.102) — sin ventaja clara. oversold(IBS<0.3): IC=-0.008 n=1237 | neutral: IC=+0.009 n=1275 | overbought(IBS>0.7): IC=+0.094 n=1523
  - _Datos_: n=4281 IC=+0.035 PNL=+342.96€

**🟡 H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: H=23h: IC=-0.115 n=172 PNL=-33.98€ → FILTRAR

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 3 celda(s) pasan gate riguroso completo de 104 evaluadas (n>=40) y 429 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=-0.012 < 0.08 — monitorear
  - _Datos_: n=322 IC=-0.012 PNL=-10.51€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=312/15 IC=+0.258 PNL=+69.34€ | BTC: n=295/15 IC=+0.200 PNL=+2.11€ | SOL: n=386/15 IC=+0.374 PNL=+325.39€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.088 n=59225 | tras_1loss IC=+0.047 n=44606 | tras_2loss IC=+0.010 n=20139/40 | gap=+0.078 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 17 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC, UPDOWN_GBM#SOL
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.154 n=24/60 | contraria IC=-0.044 n=14 | gap=+0.198 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=36, boost estimado=+0.001. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 37/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=123/40 IC=+0.044 PNL=+10.09€ | BTC#60min: n=99/40 IC=-0.015 PNL=-0.19€ | SOL#60min: n=75/40 IC=-0.019 PNL=-0.59€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.002 n=325 | contrario_BTC IC=+0.010 n=247/40 | gap=+0.011 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.172 > 0.08 con n=65 PNL=+32.96€
  - _Datos_: n=65 IC=+0.172 PNL=+32.96€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.08 con n=79 PNL=+17.43€
  - _Datos_: n=79 IC=+0.117 PNL=+17.43€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 8/25 ops en el filtro definido (IC actual=+0.160 PNL=+9.98€)
  - _Datos_: n=8 IC=+0.160 PNL=+9.98€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.337 > 0.1 con n=843 PNL=+402.22€
  - _Datos_: n=843 IC=+0.337 PNL=+402.22€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=31 IC=+0.015 PNL=+8.66€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=31 IC=+0.015 PNL=+8.66€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 12/30 ops en el filtro definido (IC actual=+0.043 PNL=+0.77€)
  - _Datos_: n=12 IC=+0.043 PNL=+0.77€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=3393 IC=+0.005 PNL=+84.25€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=3393 IC=+0.005 PNL=+84.25€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 1/15 ops en el filtro definido (IC actual=+0.008 PNL=+1.22€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.22€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=238 IC=+0.037 PNL=+16.78€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=238 IC=+0.037 PNL=+16.78€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=59 IC=-0.107 PNL=-7.47€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=59 IC=-0.107 PNL=-7.47€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=66 IC=+0.015 PNL=+2.31€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=66 IC=+0.015 PNL=+2.31€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.1 con n=453 PNL=+87.97€
  - _Datos_: n=453 IC=+0.111 PNL=+87.97€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=167 IC=+0.092 PNL=+43.27€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=167 IC=+0.092 PNL=+43.27€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=167 IC=+0.080 PNL=+16.11€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=167 IC=+0.080 PNL=+16.11€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=929 IC=+0.043 PNL=+67.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=929 IC=+0.043 PNL=+67.83€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 16/30 ops en el filtro definido (IC actual=-0.178 PNL=-2.92€)
  - _Datos_: n=16 IC=-0.178 PNL=-2.92€

**🔶 H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: SEÑAL POSITIVA en ETH (IC=+0.090 n=37) pero sin cruzar ≥2 pares más — BNB: n=10 IC=+0.042; DOGE: n=8 IC=+0.000; SOL: n=23 IC=+0.140 ✓; XRP: n=38 IC=+0.000
  - _Datos_: n=37 IC=+0.090 PNL=+14.10€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=39 IC=+0.159 PNL=+11.35€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=39 IC=+0.159 PNL=+11.35€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 4/15 ops en el filtro definido (IC actual=+0.000 PNL=-0.05€)
  - _Datos_: n=4 IC=+0.000 PNL=-0.05€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=774 IC=-0.051 PNL=-59.22€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=774 IC=-0.051 PNL=-59.22€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.08 con n=33 PNL=+9.78€
  - _Datos_: n=33 IC=+0.214 PNL=+9.78€

**⏳ H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: 30
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: 4/30 ops en el filtro definido (IC actual=+0.067 PNL=+2.07€)
  - _Datos_: n=4 IC=+0.067 PNL=+2.07€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=951 IC=+0.026 PNL=+69.24€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=951 IC=+0.026 PNL=+69.24€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=380 IC=+0.026 PNL=-4.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=380 IC=+0.026 PNL=-4.29€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.08 con n=52 PNL=+15.88€
  - _Datos_: n=52 IC=+0.130 PNL=+15.88€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.140 > 0.08 con n=98 PNL=-5.74€
  - _Datos_: n=98 IC=+0.140 PNL=-5.74€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=91 PNL=+22.87€
  - _Datos_: n=91 IC=+0.113 PNL=+22.87€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=571 IC=+0.144 PNL=+1.44€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=571 IC=+0.144 PNL=+1.44€

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
  - _Estado_: n=510 IC=+0.025 PNL=+33.89€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=510 IC=+0.025 PNL=+33.89€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.146 > 0.02 con n=162 PNL=+53.74€
  - _Datos_: n=162 IC=+0.146 PNL=+53.74€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=86 IC=-0.125 PNL=+14.04€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=86 IC=-0.125 PNL=+14.04€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.442 > 0.1 con n=551 PNL=+447.31€
  - _Datos_: n=551 IC=+0.442 PNL=+447.31€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1138 IC=+0.033 PNL=+74.86€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1138 IC=+0.033 PNL=+74.86€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.157 > 0.1 con n=648 PNL=+223.96€
  - _Datos_: n=648 IC=+0.157 PNL=+223.96€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 13/40 ops en el filtro definido (IC actual=-0.238 PNL=-7.00€)
  - _Datos_: n=13 IC=-0.238 PNL=-7.00€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=289 IC=+0.033 PNL=+35.28€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=289 IC=+0.033 PNL=+35.28€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=30 IC=-0.188 PNL=+2.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=30 IC=-0.188 PNL=+2.99€

**⏳ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: 50
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: 48/50 ops en el filtro definido (IC actual=+0.080 PNL=+1.81€)
  - _Datos_: n=48 IC=+0.080 PNL=+1.81€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=2367 IC=-0.117 PNL=+325.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2367 IC=-0.117 PNL=+325.29€

**⏳ H-CUSTOM-LATE15-PHOTO-FINISH** — GBM_LATE_15M photo finish — entrar pegado al strike es moneda al aire cobrada como favorito
  - _Hipótesis_: Detectado 2026-07-05 validando contra nuestros datos la única idea aprovechable de un artículo-anuncio de copy-bot: GBM_LATE_15M con |drift_ventana_pct|<0.02 tenía IC=-0.145 n=181 (win 35%, -9.70€), estable en ambas mitades temporales (-0.163/-0.127), monótono con la distancia (0.02-0.05: IC=+0.061; ≥0.05: IC=+0.14..0.19) y consistente en crudo y normalizado por sigma (|d_gbm|<0.1 IC=-0.081 n=244). BTC (IC=-0.163 n=90) y ETH (-0.130 n=79) concentraban el daño; SOL/XRP apenas entran en esa zona. Mecanismo: sin distancia real al strike el resultado es ~50/50 pero py_entrada ya cobra favorito. Filtro GBM_LATE_DRIFT_VENT_MIN_PCT=0.02 aplicado en shadow_predict el 2026-07-05. Esta hipótesis trackea la zona filtrada: si vuelven a aparecer ops aquí, el filtro se ha roto.
  - _Umbral_: 200
  - _Acción_: Si aparecen ops nuevas en la zona → el filtro está roto, revisar shadow_predict. Si el buffer [0.02,0.05) se vuelve negativo con n≥60 forward → subir el corte a 0.05.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=428 IC=+0.137 PNL=+156.41€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=428 IC=+0.137 PNL=+156.41€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=453 PNL=+87.97€
  - _Datos_: n=453 IC=+0.111 PNL=+87.97€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=377 IC=-0.009 PNL=-0.64€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=377 IC=-0.009 PNL=-0.64€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.08 con n=463 PNL=+279.33€
  - _Datos_: n=463 IC=+0.106 PNL=+279.33€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.149 > 0.08 con n=112 PNL=+22.15€
  - _Datos_: n=112 IC=+0.149 PNL=+22.15€

**⏳ H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: 289
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: 183/289 ops en el filtro definido (IC actual=-0.219 PNL=-6.59€)
  - _Datos_: n=183 IC=-0.219 PNL=-6.59€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=854 IC=+0.158 PNL=+480.31€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=854 IC=+0.158 PNL=+480.31€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 17/40 ops en el filtro definido (IC actual=+0.022 PNL=-1.83€)
  - _Datos_: n=17 IC=+0.022 PNL=-1.83€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=442 IC=-0.036 PNL=+5.00€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=442 IC=-0.036 PNL=+5.00€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.08 con n=384 PNL=+212.02€
  - _Datos_: n=384 IC=+0.184 PNL=+212.02€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=703 IC=-0.006 PNL=+142.88€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=703 IC=-0.006 PNL=+142.88€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=191 PNL=-24.61€
  - _Datos_: n=191 IC=+0.122 PNL=-24.61€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.243 > 0.08 con n=908 PNL=-93.03€
  - _Datos_: n=908 IC=+0.243 PNL=-93.03€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 7/40 ops en el filtro definido (IC actual=+0.019 PNL=+3.02€)
  - _Datos_: n=7 IC=+0.019 PNL=+3.02€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.115 n=76) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=76 IC=+0.115 PNL=+16.27€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.345 > 0.08 con n=56 PNL=+45.37€
  - _Datos_: n=56 IC=+0.345 PNL=+45.37€

**⏳ H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: 200
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: 198/200 ops en el filtro definido (IC actual=+0.440 PNL=+265.93€)
  - _Datos_: n=198 IC=+0.440 PNL=+265.93€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=1778 IC=+0.116 PNL=-359.99€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=1778 IC=+0.116 PNL=-359.99€

**⏳ H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: 40
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: 22/40 ops en el filtro definido (IC actual=+0.250 PNL=+16.47€)
  - _Datos_: n=22 IC=+0.250 PNL=+16.47€
