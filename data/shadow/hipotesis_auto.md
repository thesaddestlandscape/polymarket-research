# Hipótesis automáticas — 2026-07-26 01:29 UTC
_Generado por shadow_postmortem.py sobre 35784 resoluciones (PNL=+7583.71€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=2290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.200 (n=1115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.331 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2563)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=940)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.196 (n=850)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 5.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.340 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=2749)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.174)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.215 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.214 (n=522)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.266 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.605 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.228 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.364 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=706)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.230 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.565 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.635` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.635 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `8779.1187` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8779.1187 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.267 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.264 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.405 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `6042.7668` → IC=+0.177 (n=153)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 6042.7668 (IC base=+0.165)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.216 (n=466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.351 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.209 (n=386)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.198)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.170 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.575 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.575` → IC=+0.149 (n=132)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` > 0.575 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=135)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.204 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.405 (IC base=+0.149)

- **PATRÓN** `py_entrada` > `0.425` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.425 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `4102.9784` → IC=+0.198 (n=137)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 4102.9784 (IC base=+0.149)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.232 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.232 (n=229)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.323 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1888.7041` → IC=+0.231 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1888.7041 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.235 (n=187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.344 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1581.0777` → IC=+0.214 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1581.0777 (IC base=+0.210)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.182 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 8.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.64` → IC=+0.191 (n=124)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.64 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.575` → IC=+0.181 (n=142)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.575 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.199 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.127 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 17.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.162 (n=146)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.117)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.131 (n=2202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 8.0 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.474` → IC=+0.132 (n=308)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.474 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.485` → IC=+0.207 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.485 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.9759` → IC=+0.133 (n=137)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.9759 (IC base=+0.095)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.127 (n=590)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0068 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.134 (n=528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 8.0 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.4428` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4428 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` < `0.1118` → IC=+0.139 (n=250)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1118 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.155` → IC=+0.202 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.155 (IC base=+0.107)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.160 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0043 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.122 (n=411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 8.0 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.1508` → IC=+0.143 (n=113)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1508 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.222` → IC=+0.192 (n=115)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 7.222 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.5687` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.5687 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.737` → IC=+0.157 (n=138)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.737 (IC base=+0.067)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `8.398` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.398
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=543)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.382` → IC=+0.230 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.382 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.149 (n=380)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 8.0 (IC base=+0.101)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.167 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0102 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0211` → IC=+0.158 (n=320)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0211 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.153 (n=709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6483` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6483 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1132` → IC=+0.139 (n=339)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1132 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.597` → IC=+0.286 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.597 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0257` → IC=+0.160 (n=292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0257 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.164 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.158 (n=317)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 6.0 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.140)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.192 (n=1060)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0076 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.170 (n=1432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.2791` → IC=+0.197 (n=440)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.2791 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.591` → IC=+0.245 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.591 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.163 (n=1259)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0068 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.136 (n=1333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 12.0 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.9868` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.9868 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.417` → IC=+0.155 (n=279)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 8.417 (IC base=+0.123)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.139 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0049 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.4819` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.4819 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.624` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 12.624 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.36` → IC=+0.147 (n=171)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 4.36 (IC base=+0.090)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.199 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0079 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.148 (n=268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 12.0 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.1146` → IC=+0.157 (n=170)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1146 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.301` → IC=+0.201 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.301 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.543` → IC=+0.145 (n=91)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.543 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.606` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.606 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.202 (n=139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.145 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 8.0 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.156 (n=152)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.667` → IC=+0.276 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.667 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.016` → IC=+0.128 (n=377)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.016 (IC base=+0.092)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0179` → IC=+0.263 (n=374)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0179 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.239 (n=374)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.253 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.6538` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6538 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.089` → IC=+0.363 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.089 (IC base=+0.238)

- **PATRÓN** `sigma_h` < `0.0168` → IC=+0.215 (n=490)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0168 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.251 (n=491)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.238 (n=448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.6586` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6586 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.757` → IC=+0.215 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.757 (IC base=+0.216)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.149 (n=508)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0129 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.122 (n=1432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 7.0 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.4799` → IC=+0.161 (n=293)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.4799 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.514` → IC=+0.270 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.514 (IC base=+0.109)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.146 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0041 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.144 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 8.0 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.4819` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.4819 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.2` → IC=+0.212 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.2 (IC base=+0.099)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `13.023` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.023 (IC base=+0.065)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `7.928` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.928
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=435)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.017` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.017 (IC base=+0.066)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.151 (n=147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0074 (IC base=+0.064)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.151 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 6.0 (IC base=+0.064)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0209` → IC=+0.187 (n=416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0209 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0275` → IC=+0.188 (n=158)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0275 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=424)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.2665` → IC=+0.227 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2665 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.065` → IC=+0.300 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.065 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.176 (n=606)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0079 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.180 (n=426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 12.0 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `1.0308` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0308 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.657` → IC=+0.164 (n=614)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 9.657 (IC base=+0.164)

### GBM_LATE_60M
- **FILTRO** `sigma_ewma_delta_pct` < `14.597` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 14.597
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=13)

- **FILTRO** `sigma_h` > `0.0133` → IC=-0.300 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=118)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.272 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=44)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.188 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0045 (IC base=-0.008)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0034` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `sigma_h` < `0.008` → IC=-0.167 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.175 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.005 (IC base=+0.033)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0084` → IC=-0.333 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=32)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=33)

- **FILTRO** `hora_utc` < `18.0` → IC=-0.294 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.333 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` < `0.0135` → IC=-0.258 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0135
  - _Potencial_: sin este filtro IC_bueno=+0.237 (n=17)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.125 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `sigma_h` > `0.0103` → IC=-0.271 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `hora_utc` < `18.0` → IC=-0.202 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.261 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

### LEADLAG_BTC_XRP_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=155)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=155)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=145)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `total_vol_5m` < `197.886` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 197.886 (IC base=+0.031)

### ORDER_FLOW_5M#BTC#5min
- **FILTRO** `delta_ratio` |x|≤ `0.3925` → IC=-0.180 (n=23)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.3925
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=80)

### ORDER_FLOW_5M#DOGE#5min
- **FILTRO** `total_vol_5m` > `1108292.0` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `total_vol_5m` > 1108292.0
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=61)

### ORDER_FLOW_5M#XRP#5min
- **FILTRO** `delta_ratio` |x|≤ `0.4307` → IC=-0.136 (n=20)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.4307
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=45)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0105` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0105
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `sigma_h` > `0.0062` → IC=-0.365 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=25)

- **FILTRO** `T_h` < `145.8988` → IC=-0.423 (n=50)

  - _Acción_: SKIP cuando `T_h` < 145.8988
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

- **FILTRO** `pct_vs_K` |x|> `2.6724` → IC=-0.481 (n=50)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6724
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.433 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **FILTRO** `T_h` > `111.9936` → IC=-0.455 (n=20)

  - _Acción_: SKIP cuando `T_h` > 111.9936
  - _Potencial_: sin este filtro IC_bueno=-0.400 (n=8)

- **FILTRO** `T_h` < `145.9348` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `T_h` < 145.9348
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

- **FILTRO** `pct_vs_K` |x|> `3.4276` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4276
  - _Potencial_: sin este filtro IC_bueno=-0.409 (n=9)

### STREAK_FADE_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=90)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.196 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 7.0 (IC base=+0.070)

- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.070)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### STREAK_FADE_15M#SOL#15min
- **PATRÓN** `streak_len` < `4.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `streak_len` < 4.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.485 (IC base=+0.125)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.075)

- **PATRÓN** `volumen_racha` < `503163.4` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 503163.4 (IC base=+0.075)

### STREAK_FADE_5M
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

- **FILTRO** `streak_len` > `4.0` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=47)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `6441.4408` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 6441.4408
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### STREAK_MOM_5M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.250 (n=46)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=98)

- **FILTRO** `streak_len` > `4.0` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=120)

- **FILTRO** `libro_liquidez` < `3352.7321` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `libro_liquidez` < 3352.7321
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=103)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=149)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=76)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=85)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `libro_liquidez` < `8045.5084` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 8045.5084
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=30)

- **FILTRO** `libro_liquidez` < `3331.5444` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3331.5444
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=33)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

- **FILTRO** `hora_utc` < `18.0` → IC=-0.203 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

- **FILTRO** `streak_len` > `3.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=35)

- **FILTRO** `libro_liquidez` < `3688.8474` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 3688.8474
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=23)

### UPDOWN_GBM#15min
- **PATRÓN** `ibs_15` > `0.7622` → IC=+0.231 (n=426)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7622 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.1741` → IC=+0.180 (n=195)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1741 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.112` → IC=+0.159 (n=177)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 7.112 (IC base=+0.057)

### UPDOWN_GBM#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.01` → IC=-0.300 (n=28)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `sigma_h` > `0.0024` → IC=-0.333 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0024
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.03` → IC=-0.167 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.03
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `sigma_h` > `0.0018` → IC=-0.143 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0018
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### UPDOWN_GBM#60min
- **FILTRO** `sigma_h` < `0.0058` → IC=-0.208 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=67)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **FILTRO** `ibs_15` > `0.1935` → IC=-0.175 (n=38)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1935
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `ibs_15` < `0.5186` → IC=-0.204 (n=25)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5186
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `hora_utc` < `19.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `ibs_15` < `0.7622` → IC=-0.182 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7622
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.0344` → IC=-0.133 (n=28)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0344
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.124 (n=264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0063 (IC base=+0.101)

- **PATRÓN** `drift_60min` |x|≤ `0.2217` → IC=+0.138 (n=291)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.2217 (IC base=+0.101)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0855` → IC=+0.126 (n=260)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.63€ cuando `delta_ratio_macro` |x|> 0.0855 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.140 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 19.0 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.156 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 8.0 (IC base=+0.101)

- **PATRÓN** `ibs_15` > `0.7301` → IC=+0.248 (n=224)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7301 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.2571` → IC=+0.232 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2571 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.96` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 24.96 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.681` → IC=+0.156 (n=126)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 14.681 (IC base=+0.101)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.182 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0055 (IC base=+0.013)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_h` < `0.012` → IC=-0.143 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.012
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `ibs_15` > `0.6814` → IC=+0.186 (n=186)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` > 0.6814 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` < `0.6603` → IC=+0.127 (n=175)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.6603 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.389` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 22.389 (IC base=+0.048)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.143 (n=169)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.006 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.4502` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.4502 (IC base=+0.060)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `sigma_h` > `0.0204` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0204
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `sigma_h` < `0.0133` → IC=-0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=35)

- **FILTRO** `drift_15min` |x|> `0.3058` → IC=-0.136 (n=31)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3058
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1932` → IC=-0.167 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1932
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **PATRÓN** `drift_15min` |x|≤ `0.4324` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `drift_15min` |x|≤ 0.4324 (IC base=+0.044)

### UPDOWN_GBM#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0549` → IC=-0.192 (n=24)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0549
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0086` → IC=-0.154 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0086
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `drift_15min` |x|> `0.3967` → IC=-0.180 (n=23)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3967
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_ewma_delta_pct` > `23.985` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.985
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=165)

### WEEKLY_PRICE
- **FILTRO** `T_h` < `144.8242` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `T_h` < 144.8242
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

- **PATRÓN** `T_h` > `146.1132` → IC=+0.420 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.329)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `144.6415` → IC=+0.267 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 144.6415 (IC base=+0.263)

- **PATRÓN** `T_h` > `105.6124` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 105.6124 (IC base=+0.263)

- **PATRÓN** `pct_dist` |x|≤ `0.7729` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.7729 (IC base=+0.263)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `145.7688` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7688 (IC base=+0.253)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `111.9928` → IC=+0.413 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.396)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.7622 sube el IC de +0.057 a +0.231 en UPDOWN_GBM#15min (n=426). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7301 sube el IC de +0.101 a +0.248 en UPDOWN_GBM#BTC#15min (n=224). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6814 sube el IC de +0.048 a +0.186 en UPDOWN_GBM#ETH#15min (n=186). Ya aplicado como kelly_boost=+0.93€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO#XRP` — IC=+0.139 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1185 | +0.124 | +55.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1185 | +0.124 | +55.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 18 | +0.090 | +0.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 18 | +0.090 | +0.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 460 | +0.128 | +15.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 460 | +0.128 | +15.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 442 | +0.144 | +19.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 442 | +0.144 | +19.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 265 | +0.084 | +20.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 265 | +0.084 | +20.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 41 | +0.407 | +5.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 41 | +0.407 | +5.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 41 | +0.407 | +5.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 41 | +0.407 | +5.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 6387 | +0.181 | +14.94€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 4205 | +0.207 | +14.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 282 | +0.049 | -23.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 781 | +0.126 | -60.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 1119 | +0.158 | +84.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 1875 | +0.188 | +16.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1399 | +0.202 | -32.93€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 93 | +0.037 | -11.99€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 373 | +0.183 | +64.98€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 7 | +0.097 | +4.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 6 | +0.075 | +3.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 2247 | +0.170 | -31.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1385 | +0.202 | -0.28€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 93 | -0.026 | -22.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 396 | +0.128 | -29.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 373 | +0.145 | +21.02€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#SOL | 2221 | +0.187 | +22.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1384 | +0.216 | +44.74€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 94 | +0.135 | +11.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 370 | +0.129 | -32.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 373 | +0.145 | -1.22€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#XRP | 34 | +0.139 | +0.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 28 | +0.100 | -3.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 370 | +0.301 | +5.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 370 | +0.301 | +5.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 370 | +0.301 | +5.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 370 | +0.301 | +5.00€ | 0 | 0 |
| ✅ GBM_LATE_15M | 7873 | +0.095 | +2413.05€ | 0 | 4 |
| ✅ GBM_LATE_15M#15min | 7873 | +0.095 | +2413.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 1905 | +0.070 | +333.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1905 | +0.070 | +333.52€ | 0 | 5 |
| ✅ GBM_LATE_15M#ETH | 1747 | +0.074 | +299.80€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1747 | +0.074 | +299.80€ | 0 | 6 |
| ✅ GBM_LATE_15M#SOL | 2118 | +0.087 | +743.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2118 | +0.087 | +743.58€ | 1 | 3 |
| ✅ GBM_LATE_15M#XRP | 2103 | +0.143 | +1036.14€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2103 | +0.143 | +1036.14€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5085 | +0.119 | +2450.30€ | 0 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5085 | +0.119 | +2450.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1328 | +0.086 | +475.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1328 | +0.086 | +475.65€ | 0 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1327 | +0.086 | +462.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1327 | +0.086 | +462.18€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1277 | +0.092 | +517.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1277 | +0.092 | +517.63€ | 0 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1153 | +0.226 | +994.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1153 | +0.226 | +994.83€ | 0 | 10 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 267 | +0.087 | +111.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 267 | +0.087 | +111.08€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 106 | -0.028 | +14.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 106 | -0.028 | +14.50€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 144 | +0.219 | +100.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 144 | +0.219 | +100.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 5087 | +0.072 | +1411.37€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#15min | 5087 | +0.072 | +1411.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1221 | +0.038 | +157.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1221 | +0.038 | +157.78€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1234 | +0.026 | +96.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1234 | +0.026 | +96.16€ | 0 | 1 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1192 | +0.034 | +237.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1192 | +0.034 | +237.44€ | 1 | 3 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1440 | +0.171 | +919.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1440 | +0.171 | +919.99€ | 0 | 10 |
| ✅ GBM_LATE_5M | 687 | -0.033 | -0.70€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 687 | -0.033 | -0.70€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 164 | -0.030 | -11.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 164 | -0.030 | -11.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 75 | -0.188 | -14.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 75 | -0.188 | -14.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 184 | -0.086 | +8.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 184 | -0.086 | +8.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 264 | +0.049 | +16.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 264 | +0.049 | +16.12€ | 0 | 0 |
| ✅ GBM_LATE_60M | 339 | -0.107 | +6.05€ | 3 | 1 |
| ✅ GBM_LATE_60M#60min | 339 | -0.107 | +6.05€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 121 | -0.037 | +3.72€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 121 | -0.037 | +3.72€ | 3 | 1 |
| ✅ GBM_LATE_60M#ETH | 108 | -0.136 | -8.94€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 108 | -0.136 | -8.94€ | 4 | 0 |
| ✅ GBM_LATE_60M#SOL | 110 | -0.152 | +11.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 110 | -0.152 | +11.27€ | 5 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO | 9 | -0.143 | -2.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO#60min | 9 | -0.143 | -2.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 353 | -0.055 | -4.57€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 353 | -0.055 | -4.57€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 353 | -0.055 | -4.57€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 353 | -0.055 | -4.57€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 288 | +0.010 | +9.63€ | 1 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 288 | +0.010 | +9.63€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 288 | +0.010 | +9.63€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 288 | +0.010 | +9.63€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1676 | +0.010 | +8.93€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1540 | +0.006 | -3.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 215 | +0.030 | +3.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 215 | +0.030 | +3.61€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 226 | +0.000 | -2.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 226 | +0.000 | -2.22€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 267 | -0.017 | -8.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 267 | -0.017 | -8.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 330 | +0.042 | +13.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 330 | +0.042 | +13.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 211 | -0.007 | -5.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 211 | -0.007 | -5.47€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM | 150 | -0.171 | -4.78€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 62 | -0.250 | -18.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 56 | -0.276 | -17.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 6 | +0.000 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 58 | -0.183 | -0.24€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#ETH#atexpiry | 52 | -0.204 | -3.53€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 6 | +0.000 | +3.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 30 | +0.031 | +13.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 28 | +0.033 | +13.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 136 | -0.188 | -7.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 14 | +0.000 | +2.83€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 13 | +0.195 | +3.10€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 6 | +0.113 | +1.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 6 | +0.113 | +1.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 13 | +0.195 | +3.10€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 288 | +0.072 | +25.72€ | 1 | 2 |
| ✅ STREAK_FADE_15M#15min | 288 | +0.072 | +25.72€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 63 | +0.038 | -2.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 63 | +0.038 | -2.53€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 87 | +0.129 | +22.47€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 87 | +0.129 | +22.47€ | 0 | 3 |
| ✅ STREAK_FADE_15M#XRP | 138 | +0.050 | +5.79€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 138 | +0.050 | +5.79€ | 0 | 2 |
| ✅ STREAK_FADE_5M | 246 | -0.048 | -24.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 246 | -0.048 | -24.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 47 | -0.153 | -8.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 3 | 0 |
| ✅ STREAK_FADE_5M#SOL | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 105 | -0.023 | -9.27€ | 0 | 0 |
| 🚫 STREAK_MOM_5M | 320 | -0.059 | -26.41€ | 5 | 0 |
| ✅ STREAK_MOM_5M#5min | 320 | -0.059 | -26.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 107 | -0.060 | -7.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 107 | -0.060 | -7.33€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 115 | -0.013 | -5.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 115 | -0.013 | -5.74€ | 2 | 0 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 5 | 0 |
| 🚫 STRUCT_NO_15M | 15 | -0.199 | -4.68€ | 0 | 0 |
| 🚫 STRUCT_NO_15M#15min | 15 | -0.199 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 2623 | +0.036 | +245.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2360 | +0.055 | +283.75€ | 0 | 3 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 130 | -0.061 | -11.21€ | 6 | 0 |
| ✅ UPDOWN_GBM#BNB | 266 | +0.060 | +55.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 266 | +0.060 | +55.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 561 | +0.052 | +63.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 477 | +0.087 | +77.95€ | 1 | 10 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 43 | -0.078 | -6.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 208 | +0.029 | +16.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 205 | +0.031 | +17.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1038 | +0.040 | +77.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 944 | +0.055 | +89.38€ | 0 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 55 | -0.026 | -3.07€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 267 | -0.032 | +2.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 198 | +0.000 | +8.67€ | 4 | 1 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 32 | -0.088 | -1.46€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 281 | +0.037 | +31.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 270 | +0.048 | +34.63€ | 4 | 0 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 166 | +0.298 | +31.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 166 | +0.298 | +31.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 78 | +0.300 | +14.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 78 | +0.300 | +14.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 88 | +0.289 | +16.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 88 | +0.289 | +16.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1794 | +0.156 | +810.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1794 | +0.156 | +810.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 171 | +0.199 | +101.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 171 | +0.199 | +101.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 192 | +0.113 | +32.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 192 | +0.113 | +32.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 157 | +0.217 | +109.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 157 | +0.217 | +109.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 352 | +0.175 | +149.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 352 | +0.175 | +149.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 432 | +0.092 | +115.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 432 | +0.092 | +115.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 490 | +0.177 | +302.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 490 | +0.177 | +302.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 15 | +0.066 | +1.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 15 | +0.066 | +1.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 15 | +0.066 | +1.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 15 | +0.066 | +1.34€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M | 84 | -0.209 | -18.89€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#5min | 84 | -0.209 | -18.89€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BNB | 13 | -0.195 | -5.11€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BNB#5min | 13 | -0.195 | -5.11€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 14 | -0.087 | -1.98€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 14 | -0.087 | -1.98€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 13 | -0.108 | -2.68€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 13 | -0.108 | -2.68€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#ETH | 18 | -0.225 | -4.88€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#ETH#5min | 18 | -0.225 | -4.88€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 13 | -0.065 | -1.58€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 13 | -0.065 | -1.58€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 13 | -0.108 | -2.67€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 13 | -0.108 | -2.67€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 388 | +0.208 | +76.09€ | 1 | 1 |
| ✅ WEEKLY_PRICE#BTC | 112 | +0.140 | -9.66€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 109 | +0.149 | -6.87€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 167 | +0.287 | +92.61€ | 0 | 1 |