# Hipótesis automáticas — 2026-07-16 00:12 UTC
_Generado por shadow_postmortem.py sobre 16136 resoluciones (PNL=+3267.44€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.184 (n=804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.215 (n=388)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.695` → IC=+0.287 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.695 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=993)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `4419.7043` → IC=+0.184 (n=564)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 4419.7043 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.189 (n=439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 16.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.202 (n=317)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.326 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=1044)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `7407.0697` → IC=+0.188 (n=306)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 7407.0697 (IC base=+0.163)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.200 (n=188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.615` → IC=+0.248 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.615 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `11311.7874` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 11311.7874 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.236 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.224 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.382 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `7259.2748` → IC=+0.213 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7259.2748 (IC base=+0.204)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` < `18.0` → IC=+0.196 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 18.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.565 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.635` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.635 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `6840.9445` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 6840.9445 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.286 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.158)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.425 (IC base=+0.158)

- **PATRÓN** `py_entrada` > `0.395` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.395 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `7670.1712` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7670.1712 (IC base=+0.158)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.238 (n=185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.237 (n=188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.246 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.357 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `3824.1428` → IC=+0.213 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3824.1428 (IC base=+0.207)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` < `18.0` → IC=+0.235 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4587.4443` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 4587.4443 (IC base=+0.138)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.240 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.218 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.625` → IC=+0.277 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.625 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.239 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.206 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.247 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.200)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `20.0` → IC=+0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 20.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.289 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` < `0.585` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.585 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `2428.8761` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2428.8761 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.143 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.087)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.087)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.087)

### GBM_LATE_15M
- **PATRÓN** `dist_vwap_pct` > `0.6272` → IC=+0.130 (n=125)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.6272 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.178` → IC=+0.207 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.178 (IC base=+0.109)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.133 (n=1206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0091 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.128 (n=1292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 12.0 (IC base=+0.104)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.2945` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2945 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.305` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.305 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.176` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.176 (IC base=+0.060)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `sigma_ewma_delta_pct` < `7.25` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 7.25
  - _Potencial_: sin este filtro IC_bueno=+0.266 (n=45)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.146 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0045 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.6749` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.6749 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.25` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.25 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.7664` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.7664 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.518` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 7.518 (IC base=+0.064)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `8.445` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.445
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=141)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.144 (n=206)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0108 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.141 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 16.0 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.034` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.034 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.142 (n=400)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0135 (IC base=+0.129)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.134 (n=454)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0093 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.176 (n=331)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.129)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` > `0.0237` → IC=+0.180 (n=198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0237 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.153 (n=390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 8.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.153 (n=292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6733` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6733 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.138` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.138 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0269` → IC=+0.195 (n=152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0269 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.242 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.3501` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.3501 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` < `0.9583` → IC=+0.134 (n=170)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.9583 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.722` → IC=+0.126 (n=145)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 7.722 (IC base=+0.162)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.220 (n=319)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.170 (n=473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 13.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.168 (n=720)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 18.0 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.1538` → IC=+0.197 (n=265)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1538 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.022` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.022 (IC base=+0.160)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.176 (n=718)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0048 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.165 (n=496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 12.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.173 (n=273)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 6.0 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` < `0.4453` → IC=+0.193 (n=489)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.4453 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.097` → IC=+0.259 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.097 (IC base=+0.160)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.146 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0027 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.167 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 13.0 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.5737` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5737 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.074` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.074 (IC base=+0.116)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.172 (n=181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0028 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.157 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 8.0 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1925` → IC=+0.140 (n=123)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1925 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.397` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.397 (IC base=+0.138)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.147 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0044 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.236 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.159 (n=136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 12.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.165 (n=195)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 18.0 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.3858` → IC=+0.192 (n=63)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.3858 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.752` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.752 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.138 (n=161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0067 (IC base=+0.129)

- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.143 (n=183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0037 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.177 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.162 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 6.0 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.7664` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.7664 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `1.433` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 1.433 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.012` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.012 (IC base=+0.129)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `3.243` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.243
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=107)

- **PATRÓN** `sigma_h` > `0.013` → IC=+0.208 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.013 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.158 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 18.0 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.4593` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.4593 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `1.0657` → IC=+0.155 (n=143)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 1.0657 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.082` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.082 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.191 (n=66)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0082 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.157 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` < `0.1968` → IC=+0.172 (n=114)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1968 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.243` → IC=+0.161 (n=107)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.243 (IC base=+0.102)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0187` → IC=+0.278 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0187 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.282 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.253)

- **PATRÓN** `dist_vwap_pct` > `0.8165` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8165 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.099` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.099 (IC base=+0.253)

- **PATRÓN** `sigma_h` < `0.0161` → IC=+0.289 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0161 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.326 (n=159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.296 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.310 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` < `0.5686` → IC=+0.309 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5686 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.18` → IC=+0.302 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.18 (IC base=+0.289)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0149` → IC=+0.190 (n=217)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0149 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.123 (n=593)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 16.0 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.7118` → IC=+0.170 (n=116)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.7118 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.1427` → IC=+0.146 (n=221)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1427 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.68` → IC=+0.316 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.68 (IC base=+0.111)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.5186` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.5186 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1146` → IC=+0.125 (n=54)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1146 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.972` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 10.972 (IC base=+0.087)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.123 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 17.0 (IC base=+0.061)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.155 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0039 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.266` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.266 (IC base=+0.052)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` < `7.311` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 7.311
  - _Potencial_: sin este filtro IC_bueno=+0.360 (n=41)

- **FILTRO** `sigma_ewma_delta_pct` > `3.17` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.17
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=108)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.134 (n=69)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0129 (IC base=+0.081)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.149 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 8.0 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.9118` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.9118 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.2565` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2565 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.311` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.311 (IC base=+0.081)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.129 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 6.0 (IC base=+0.035)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.216 (n=188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.254 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.5779` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5779 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.958` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.958 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.223` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.223 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.0237` → IC=+0.240 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0237 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.220 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.3325` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.3325 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` < `0.5085` → IC=+0.175 (n=164)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.5085 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.517` → IC=+0.185 (n=128)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 2.517 (IC base=+0.190)

### GBM_LATE_60M
- **FILTRO** `dist_vwap_pct` < `0.1109` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1109
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `sigma_ewma_delta_pct` < `16.76` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 16.76
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=3)

- **FILTRO** `sigma_h` > `0.0133` → IC=-0.300 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=118)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.272 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=44)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.152 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0047 (IC base=-0.017)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0086` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0086
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=52)

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

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.176 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0053 (IC base=+0.043)

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

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=-0.080)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` < `0.485` → IC=+0.150 (n=18)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.485 (IC base=+0.057)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.505 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2187.757` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2187.757 (IC base=+0.057)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.189 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.131)

- **PATRÓN** `btc_momentum` |x|≤ `0.03` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `btc_momentum` |x|≤ 0.03 (IC base=+0.131)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` < `0.485` → IC=+0.150 (n=18)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.485 (IC base=+0.057)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.505 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2187.757` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2187.757 (IC base=+0.057)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.189 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.131)

- **PATRÓN** `btc_momentum` |x|≤ `0.03` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `btc_momentum` |x|≤ 0.03 (IC base=+0.131)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=74)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `total_vol_5m` < `197.886` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 197.886 (IC base=+0.031)

### ORDER_FLOW_5M#BTC#5min
- **FILTRO** `delta_ratio` |x|≤ `0.3925` → IC=-0.180 (n=23)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.3925
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=80)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=24)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.192 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 4.0 (IC base=+0.000)

### ORDER_FLOW_5M#DOGE#5min
- **FILTRO** `delta_ratio` |x|≤ `0.4217` → IC=-0.140 (n=23)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.4217
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=70)

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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **FILTRO** `sigma_h` > `0.0055` → IC=-0.363 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.231 (n=24)

- **FILTRO** `T_h` < `144.7669` → IC=-0.432 (n=42)

  - _Acción_: SKIP cuando `T_h` < 144.7669
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=23)

- **FILTRO** `pct_vs_K` |x|> `2.6724` → IC=-0.480 (n=48)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6724
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.231 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=-0.211)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.429 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **FILTRO** `T_h` > `98.7549` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `T_h` > 98.7549
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

- **FILTRO** `T_h` < `145.9196` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `T_h` < 145.9196
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

- **FILTRO** `pct_vs_K` |x|> `3.4276` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4276
  - _Potencial_: sin este filtro IC_bueno=-0.409 (n=9)

### STREAK_FADE_15M
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.186 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 11.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.505 (IC base=+0.110)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `streak_len` < 4.0 (IC base=+0.110)

- **PATRÓN** `regimen_ma_toques` > `3.0` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `regimen_ma_toques` > 3.0 (IC base=+0.110)

- **PATRÓN** `volumen_racha` < `249969.2` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 249969.2 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1959.3298` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 1959.3298 (IC base=+0.110)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.200 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.077)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.485 (IC base=+0.077)

- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.077)

- **PATRÓN** `volumen_racha` < `234964.8` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_racha` < 234964.8 (IC base=+0.077)

### STREAK_FADE_15M#SOL#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.485 (IC base=+0.175)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=21)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.051)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.012)

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
- **FILTRO** `py_entrada` < `0.515` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `libro_liquidez` < `7137.8206` → IC=-0.150 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7137.8206
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `hora_utc` < `18.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

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

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

- **FILTRO** `libro_liquidez` < `3416.5722` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3416.5722
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **PATRÓN** `libro_liquidez` > `3531.2061` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3531.2061 (IC base=-0.007)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.150 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=61)

### STREAK_MOM_5M
- **FILTRO** `hora_utc` > `17.0` → IC=-0.132 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=108)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.250 (n=46)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=98)

- **FILTRO** `streak_len` > `4.0` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=120)

- **FILTRO** `libro_liquidez` < `3352.7321` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `libro_liquidez` < 3352.7321
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=103)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.141 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=128)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=76)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=74)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.133 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

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

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.140 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 9.0 (IC base=+0.041)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` > 0.505 (IC base=+0.041)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.041)

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
- **PATRÓN** `ibs_15` > `0.5859` → IC=+0.136 (n=352)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` > 0.5859 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7448` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.7448 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.5087` → IC=+0.147 (n=165)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.5087 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.541` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.541 (IC base=+0.026)

- **PATRÓN** `ibs_15` < `0.0265` → IC=+0.121 (n=138)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.61€ cuando `ibs_15` < 0.0265 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `0.9263` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.9263 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` < `16.748` → IC=+0.133 (n=137)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 16.748 (IC base=+0.048)

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

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0182` → IC=-0.150 (n=18)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0182
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `hora_utc` < `20.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `ibs_15` < `0.7622` → IC=-0.150 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7622
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.0522` → IC=-0.167 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0522
  - _Potencial_: sin este filtro IC_bueno=+0.180 (n=23)

- **PATRÓN** `drift_60min` |x|≤ `0.2412` → IC=+0.130 (n=187)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.2412 (IC base=+0.076)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.158 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.076)

- **PATRÓN** `ibs_15` < `0.9252` → IC=+0.133 (n=148)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.67€ cuando `ibs_15` < 0.9252 (IC base=+0.076)

- **PATRÓN** `ibs_15` > `0.6323` → IC=+0.193 (n=148)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.97€ cuando `ibs_15` > 0.6323 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.7736` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7736 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.517` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.517 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.986` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 5.986 (IC base=+0.076)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0535` → IC=+0.129 (n=33)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.64€ cuando `pct_spot_vs_ref` |x|≤ 0.0535 (IC base=+0.022)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.289 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.022)

- **PATRÓN** `ibs_15` < `0.0522` → IC=+0.180 (n=23)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` < 0.0522 (IC base=+0.022)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_h` < `0.012` → IC=-0.143 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.012
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

- **FILTRO** `ibs_15` < `0.8328` → IC=-0.206 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8328
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `sigma_ewma_delta_pct` < `21.876` → IC=-0.140 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 21.876
  - _Potencial_: sin este filtro IC_bueno=+0.333 (n=4)

- **PATRÓN** `ibs_15` > `0.7617` → IC=+0.184 (n=93)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.92€ cuando `ibs_15` > 0.7617 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.5087` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.5087 (IC base=+0.022)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.123 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0059 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `0.974` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.974 (IC base=+0.048)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.133` → IC=-0.167 (n=19)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.133
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `ibs_15` > `0.2558` → IC=-0.132 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2558
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `sigma_h` > `0.0204` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0204
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

- **FILTRO** `drift_15min` |x|> `0.3239` → IC=-0.145 (n=29)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3239
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1932` → IC=-0.155 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1932
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `drift_60min` |x|> `0.4251` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.4251
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

- **FILTRO** `drift_15min` |x|> `0.5673` → IC=-0.140 (n=23)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5673
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=24)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0905` → IC=-0.147 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0905
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `hora_utc` < `22.0` → IC=-0.150 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 22.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### UPDOWN_GBM#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0818` → IC=-0.182 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0818
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `sigma_h` > `0.0147` → IC=-0.150 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0147
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `sigma_h` < `0.0205` → IC=-0.132 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0205
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `drift_15min` |x|> `0.4528` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4528
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `ibs_15` > `0.0669` → IC=-0.150 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0669
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=35)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0112 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.0172` → IC=+0.132 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0172 (IC base=+0.097)

- **PATRÓN** `drift_15min` |x|≤ `0.7907` → IC=+0.125 (n=30)

  - _Acción_: Kelly boost +0.62€ cuando `drift_15min` |x|≤ 0.7907 (IC base=+0.097)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1253` → IC=+0.125 (n=30)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.62€ cuando `delta_ratio_macro` |x|> 0.1253 (IC base=+0.097)

- **PATRÓN** `ibs_15` < `0.0669` → IC=+0.149 (n=35)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.74€ cuando `ibs_15` < 0.0669 (IC base=+0.097)

### WEEKLY_PRICE
- **FILTRO** `T_h` < `144.7646` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `T_h` < 144.7646
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=22)

- **PATRÓN** `T_h` > `87.9936` → IC=+0.293 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9936 (IC base=+0.279)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `144.6231` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 144.6231 (IC base=+0.238)

- **PATRÓN** `T_h` > `144.7029` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 144.7029 (IC base=+0.238)

- **PATRÓN** `pct_dist` |x|≤ `2.3456` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 2.3456 (IC base=+0.238)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `135.9981` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.9981 (IC base=+0.218)

- **PATRÓN** `pct_dist` |x|≤ `2.4966` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 2.4966 (IC base=+0.218)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` < `146.1132` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 146.1132 (IC base=+0.318)

- **PATRÓN** `T_h` > `111.9928` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.318)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS > 0.6323 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.193 n=148). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS < 0.0522 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.180 n=23). Confirma señal de reversión media → alinear con BUY_YES.
- **H-IBS-UPDOWN_GBM#ETH#15min**: IBS > 0.7617 correlaciona con éxito en UPDOWN_GBM#ETH#15min (IC=+0.184 n=93). Confirma señal de reversión media → alinear con BUY_NO.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO#SOL#240min` — IC=+0.083 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ FAVORITO_CONFIRMADO | 2349 | +0.173 | -53.76€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#15min | 1512 | +0.209 | +13.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 100 | +0.020 | -15.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 338 | +0.085 | -56.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 399 | +0.148 | +4.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 682 | +0.178 | -16.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 506 | +0.201 | -17.67€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 33 | +0.071 | -2.63€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 133 | +0.152 | +7.13€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#ETH | 835 | +0.174 | +1.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 501 | +0.218 | +23.36€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 33 | -0.100 | -11.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 168 | +0.100 | -22.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 133 | +0.167 | +12.69€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 825 | +0.169 | -34.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 498 | +0.210 | +11.44€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 34 | +0.083 | -0.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 160 | +0.093 | -30.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 133 | +0.122 | -14.99€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 7 | -0.019 | -3.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 7 | -0.019 | -3.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 26 | +0.250 | -2.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 26 | +0.250 | -2.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 26 | +0.250 | -2.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 26 | +0.250 | -2.28€ | 0 | 0 |
| ✅ GBM_LATE_15M | 4726 | +0.103 | +1476.07€ | 0 | 4 |
| ✅ GBM_LATE_15M#15min | 4726 | +0.103 | +1476.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 1134 | +0.065 | +161.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1134 | +0.065 | +161.66€ | 0 | 3 |
| ✅ GBM_LATE_15M#ETH | 1141 | +0.077 | +202.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1141 | +0.077 | +202.11€ | 1 | 5 |
| ✅ GBM_LATE_15M#SOL | 1261 | +0.111 | +516.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1261 | +0.111 | +516.32€ | 1 | 6 |
| ✅ GBM_LATE_15M#XRP | 1190 | +0.155 | +595.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1190 | +0.155 | +595.98€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 1968 | +0.151 | +1156.42€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 1968 | +0.151 | +1156.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 504 | +0.113 | +247.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 504 | +0.113 | +247.99€ | 0 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 521 | +0.129 | +244.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 521 | +0.129 | +244.42€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 532 | +0.114 | +239.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 532 | +0.114 | +239.12€ | 1 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 411 | +0.272 | +424.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 411 | +0.272 | +424.89€ | 0 | 10 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 53 | +0.082 | +14.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 53 | +0.082 | +14.19€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 8 | +0.040 | +0.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 8 | +0.040 | +0.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 28 | +0.300 | +17.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 28 | +0.300 | +17.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 1930 | +0.088 | +568.21€ | 0 | 5 |
| ✅ GBM_LATE_15M_TARDIO#15min | 1930 | +0.088 | +568.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 478 | +0.060 | +87.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 478 | +0.060 | +87.26€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 440 | +0.018 | +12.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 440 | +0.018 | +12.66€ | 0 | 2 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 464 | +0.056 | +85.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 464 | +0.056 | +85.26€ | 2 | 6 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 548 | +0.196 | +383.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 548 | +0.196 | +383.03€ | 0 | 10 |
| ✅ GBM_LATE_5M | 11 | -0.021 | -0.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 11 | -0.021 | -0.62€ | 0 | 0 |
| ✅ GBM_LATE_60M | 326 | -0.116 | +3.81€ | 4 | 1 |
| ✅ GBM_LATE_60M#60min | 326 | -0.116 | +3.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 114 | -0.035 | +5.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 114 | -0.035 | +5.51€ | 4 | 1 |
| ✅ GBM_LATE_60M#ETH | 102 | -0.164 | -12.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 102 | -0.164 | -12.97€ | 4 | 0 |
| ✅ GBM_LATE_60M#SOL | 110 | -0.152 | +11.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 110 | -0.152 | +11.27€ | 5 | 1 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO | 9 | -0.143 | -2.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO#60min | 9 | -0.143 | -2.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 44 | +0.217 | +18.78€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 44 | +0.217 | +18.78€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 44 | +0.217 | +18.78€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 44 | +0.217 | +18.78€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 131 | +0.094 | +28.25€ | 0 | 6 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 131 | +0.094 | +28.25€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 131 | +0.094 | +28.25€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 131 | +0.094 | +28.25€ | 0 | 6 |
| ✅ ORDER_FLOW_5M | 1604 | +0.012 | +12.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1468 | +0.007 | -0.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 195 | +0.048 | +7.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 195 | +0.048 | +7.22€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 2 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 213 | +0.002 | -1.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 213 | +0.002 | -1.59€ | 2 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 255 | -0.021 | -8.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 255 | -0.021 | -8.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 321 | +0.039 | +12.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 321 | +0.039 | +12.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 193 | -0.003 | -4.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 193 | -0.003 | -4.19€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM | 147 | -0.164 | -3.25€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM#BTC | 62 | -0.250 | -18.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 56 | -0.276 | -17.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 6 | +0.000 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 55 | -0.167 | +1.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 50 | -0.192 | -2.51€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 5 | +0.018 | +3.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 30 | +0.031 | +13.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 28 | +0.033 | +13.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 134 | -0.184 | -6.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 13 | +0.022 | +3.34€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 10 | +0.208 | +4.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 10 | +0.208 | +4.00€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 200 | +0.094 | +25.14€ | 0 | 10 |
| ✅ STREAK_FADE_15M#15min | 200 | +0.094 | +25.14€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 42 | +0.068 | -2.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 42 | +0.068 | -2.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 70 | +0.181 | +28.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 70 | +0.181 | +28.87€ | 0 | 2 |
| ✅ STREAK_FADE_15M#XRP | 88 | +0.033 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 88 | +0.033 | -1.71€ | 1 | 2 |
| ✅ STREAK_FADE_5M | 246 | -0.048 | -24.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 246 | -0.048 | -24.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 47 | -0.153 | -8.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 6 | 0 |
| ✅ STREAK_FADE_5M#SOL | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 94 | -0.021 | -7.62€ | 2 | 1 |
| ✅ STREAK_FADE_5M#XRP | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 105 | -0.023 | -9.27€ | 1 | 0 |
| 🚫 STREAK_MOM_5M | 309 | -0.056 | -23.67€ | 6 | 0 |
| ✅ STREAK_MOM_5M#5min | 309 | -0.056 | -23.67€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 103 | -0.052 | -6.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 103 | -0.052 | -6.34€ | 2 | 0 |
| ✅ STREAK_MOM_5M#SOL | 108 | -0.009 | -3.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 108 | -0.009 | -3.98€ | 2 | 3 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 5 | 0 |
| 🚫 STRUCT_NO_15M | 15 | -0.199 | -4.68€ | 0 | 0 |
| 🚫 STRUCT_NO_15M#15min | 15 | -0.199 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 1575 | +0.010 | +72.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1317 | +0.037 | +109.33€ | 0 | 7 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 127 | -0.058 | -10.76€ | 7 | 0 |
| ✅ UPDOWN_GBM#BNB | 81 | +0.066 | +17.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 81 | +0.066 | +17.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 408 | +0.027 | +27.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 327 | +0.065 | +40.43€ | 1 | 10 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 42 | -0.068 | -6.16€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 16 | -0.089 | +2.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 55 | +0.009 | -1.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 52 | +0.018 | -0.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 756 | +0.018 | +36.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 663 | +0.035 | +47.20€ | 1 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 54 | -0.018 | -2.56€ | 3 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 170 | -0.087 | -14.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 102 | -0.058 | -7.39€ | 7 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 31 | -0.106 | -2.03€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 103 | +0.005 | +8.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 92 | +0.032 | +12.20€ | 5 | 5 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 43 | -0.189 | +2.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 9 | +0.102 | -0.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 9 | +0.102 | -0.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 6 | +0.075 | +0.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 6 | +0.075 | +0.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 73 | +0.193 | +22.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 73 | +0.193 | +22.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 5 | -0.018 | +2.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 5 | -0.018 | +2.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 12 | +0.129 | +4.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 12 | +0.129 | +4.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 19 | +0.204 | +2.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 19 | +0.204 | +2.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 27 | +0.155 | +8.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 27 | +0.155 | +8.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 9 | +0.102 | +2.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 9 | +0.102 | +2.63€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 256 | +0.120 | +13.84€ | 1 | 1 |
| ✅ WEEKLY_PRICE#BTC | 76 | +0.077 | -9.85€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 73 | +0.087 | -8.24€ | 0 | 2 |
| ✅ WEEKLY_PRICE#SOL | 107 | +0.170 | +31.93€ | 0 | 2 |