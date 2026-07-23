# Hipótesis automáticas — 2026-07-23 07:17 UTC
_Generado por shadow_postmortem.py sobre 30448 resoluciones (PNL=+6851.55€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=1682)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.333 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=2158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.212 (n=718)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.343 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=2343)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `6051.681` → IC=+0.176 (n=953)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 6051.681 (IC base=+0.175)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.227 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.218 (n=371)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.270 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.605 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.239 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.376 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.203)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.274 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.215)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.565 (IC base=+0.215)

- **PATRÓN** `py_entrada` > `0.635` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.635 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `8877.3756` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8877.3756 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.316 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.258 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.405 (IC base=+0.163)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.232 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.351 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `4236.3867` → IC=+0.226 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4236.3867 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.229 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.370 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.208)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.655 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=112)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `5754.5746` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5754.5746 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.164 (n=102)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.405 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.365` → IC=+0.144 (n=133)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` > 0.365 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4207.6295` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 4207.6295 (IC base=+0.140)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.255 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.332 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1873.3412` → IC=+0.252 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1873.3412 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.348 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.212)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.239 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.605 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.121 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 17.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=130)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.111)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=2175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.6506` → IC=+0.131 (n=220)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.6506 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.604` → IC=+0.220 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.604 (IC base=+0.114)

- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.129 (n=910)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0133 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.2669` → IC=+0.129 (n=397)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.2669 (IC base=+0.098)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.4215` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.4215 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.193` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.193 (IC base=+0.095)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.169 (n=146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0044 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.9362` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9362 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.1625` → IC=+0.144 (n=99)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1625 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.253` → IC=+0.223 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.253 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.6297` → IC=+0.143 (n=82)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.6297 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.275` → IC=+0.175 (n=112)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 7.275 (IC base=+0.066)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `9.242` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.242
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=418)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.135 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 17.0 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.561` → IC=+0.242 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.561 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.145 (n=482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 12.0 (IC base=+0.108)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.161 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0103 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.015` → IC=+0.158 (n=437)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.015 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.5799` → IC=+0.220 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5799 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.11` → IC=+0.147 (n=284)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.11 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.597` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.597 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.160 (n=248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0096 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0269` → IC=+0.163 (n=247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0269 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.3699` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3699 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.672` → IC=+0.128 (n=100)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 5.672 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.771` → IC=+0.137 (n=406)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.771 (IC base=+0.150)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.223 (n=464)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.178 (n=1248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.2733` → IC=+0.205 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2733 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.083` → IC=+0.281 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.083 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.166 (n=1040)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0072 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.143 (n=1080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 12.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.140 (n=598)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 6.0 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.9674` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.9674 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.7303` → IC=+0.134 (n=1556)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.7303 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.174` → IC=+0.156 (n=309)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 6.174 (IC base=+0.132)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.149 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 8.0 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.4456` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4456 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.142` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 13.142 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.88` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.88 (IC base=+0.095)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.230 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.177 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 12.0 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6746` → IC=+0.205 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6746 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.776` → IC=+0.242 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.776 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6008` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6008 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.166` → IC=+0.194 (n=106)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 7.166 (IC base=+0.093)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.207 (n=172)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.150 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 8.0 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1896` → IC=+0.160 (n=145)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1896 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.848` → IC=+0.283 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.848 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.173 (n=163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0082 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.141 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` < `0.7304` → IC=+0.122 (n=347)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.7304 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.158` → IC=+0.121 (n=338)

  - _Acción_: Kelly boost +0.60€ cuando `sigma_ewma_delta_pct` < 7.158 (IC base=+0.102)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0173` → IC=+0.264 (n=337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0173 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.249 (n=337)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.260 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.243 (n=305)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.5816` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5816 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.065` → IC=+0.379 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.065 (IC base=+0.242)

- **PATRÓN** `sigma_h` < `0.0188` → IC=+0.241 (n=396)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0188 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.249 (n=396)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.249 (n=360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.1691` → IC=+0.346 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1691 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.933` → IC=+0.242 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.933 (IC base=+0.237)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.170 (n=440)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0134 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=1225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.4452` → IC=+0.157 (n=284)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.4452 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.1075` → IC=+0.135 (n=797)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1075 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.775` → IC=+0.280 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.775 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.4306` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.4306 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.358` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.358 (IC base=+0.096)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.139 (n=106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0039 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.804` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.804 (IC base=+0.074)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `6.945` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.945
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=339)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.194` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.194 (IC base=+0.076)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.126 (n=327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0109 (IC base=+0.064)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.154 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 6.0 (IC base=+0.064)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.02` → IC=+0.207 (n=373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.02 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.014` → IC=+0.204 (n=282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.014 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.5912` → IC=+0.260 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5912 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.266` → IC=+0.323 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.266 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.019` → IC=+0.179 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.019 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.177 (n=502)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0085 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.197 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.1938` → IC=+0.236 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1938 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.223` → IC=+0.173 (n=488)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 10.223 (IC base=+0.175)

### GBM_LATE_60M
- **FILTRO** `sigma_ewma_delta_pct` < `13.491` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 13.491
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

- **FILTRO** `sigma_h` > `0.0133` → IC=-0.300 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=118)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.272 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=44)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.145 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0051 (IC base=-0.017)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.132 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.175 (n=38)

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

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.175 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0053 (IC base=+0.026)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=146)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=73)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=146)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=73)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=129)

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
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=81)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.181 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 14.0 (IC base=+0.090)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `streak_len` < 4.0 (IC base=+0.090)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=81)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `2400.9155` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2400.9155 (IC base=+0.090)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.077)

- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.077)

- **PATRÓN** `volumen_racha` < `503163.4` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_racha` < 503163.4 (IC base=+0.077)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### STREAK_FADE_15M#SOL#15min
- **PATRÓN** `streak_len` < `4.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `streak_len` < 4.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.485 (IC base=+0.138)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `hora_utc` < `9.0` → IC=+0.167 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 9.0 (IC base=+0.078)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.485 (IC base=+0.078)

- **PATRÓN** `regimen_ma_toques` > `3.0` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `regimen_ma_toques` > 3.0 (IC base=+0.078)

- **PATRÓN** `volumen_racha` < `509738.3` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 509738.3 (IC base=+0.078)

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

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=76)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=83)

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
- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.231 (n=374)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1676` → IC=+0.178 (n=169)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1676 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.672` → IC=+0.180 (n=101)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 12.672 (IC base=+0.055)

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
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=29)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.125 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0078 (IC base=+0.102)

- **PATRÓN** `drift_60min` |x|≤ `0.2244` → IC=+0.137 (n=268)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.2244 (IC base=+0.102)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.127 (n=269)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.171 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 8.0 (IC base=+0.102)

- **PATRÓN** `ibs_15` > `0.6354` → IC=+0.223 (n=229)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6354 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.2402` → IC=+0.244 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2402 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.299` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 14.299 (IC base=+0.102)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.019)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_h` < `0.012` → IC=-0.143 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.012
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `ibs_15` > `0.6794` → IC=+0.189 (n=162)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` > 0.6794 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` < `0.6252` → IC=+0.129 (n=130)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.6252 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `33.732` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 33.732 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.4501` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.4501 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.277` → IC=+0.128 (n=154)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 8.277 (IC base=+0.052)

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

### UPDOWN_GBM#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0748` → IC=-0.196 (n=21)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0748
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `sigma_h` > `0.0141` → IC=-0.167 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0141
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `drift_15min` |x|> `0.4528` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4528
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **FILTRO** `sigma_ewma_delta_pct` > `13.781` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.781
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=108)

### WEEKLY_PRICE
- **FILTRO** `T_h` < `144.8242` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `T_h` < 144.8242
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

- **PATRÓN** `T_h` < `111.9959` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9959 (IC base=+0.316)

- **PATRÓN** `T_h` > `146.1118` → IC=+0.387 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.316)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `144.6415` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 144.6415 (IC base=+0.258)

- **PATRÓN** `T_h` > `111.9936` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9936 (IC base=+0.258)

- **PATRÓN** `pct_dist` |x|≤ `0.836` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.836 (IC base=+0.258)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `135.9981` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 135.9981 (IC base=+0.246)

- **PATRÓN** `T_h` > `145.7688` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7688 (IC base=+0.246)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` < `146.1426` → IC=+0.390 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 146.1426 (IC base=+0.374)

- **PATRÓN** `T_h` > `87.9977` → IC=+0.385 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9977 (IC base=+0.374)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.055 a +0.231 en UPDOWN_GBM#15min (n=374). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.6354 sube el IC de +0.102 a +0.223 en UPDOWN_GBM#BTC#15min (n=229). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6794 sube el IC de +0.040 a +0.189 en UPDOWN_GBM#ETH#15min (n=162). Ya aplicado como kelly_boost=+0.95€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 830 | +0.127 | +35.48€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 830 | +0.127 | +35.48€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 9 | +0.061 | +1.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 9 | +0.061 | +1.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 313 | +0.135 | +9.53€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 313 | +0.135 | +9.53€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 319 | +0.148 | +13.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 319 | +0.148 | +13.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 189 | +0.076 | +10.92€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 189 | +0.076 | +10.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 23 | +0.340 | +1.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 23 | +0.340 | +1.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 23 | +0.340 | +1.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 23 | +0.340 | +1.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 5315 | +0.187 | +88.60€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#15min | 3484 | +0.215 | +87.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 229 | +0.054 | -14.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 678 | +0.118 | -67.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 924 | +0.165 | +83.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 1556 | +0.193 | +34.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1162 | +0.208 | -11.35€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 76 | +0.051 | -7.27€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 308 | +0.187 | +56.99€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH | 1878 | +0.178 | +15.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1147 | +0.214 | +40.93€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 76 | -0.026 | -17.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 347 | +0.125 | -28.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 308 | +0.152 | +20.46€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#SOL | 1852 | +0.191 | +33.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1150 | +0.224 | +58.19€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 77 | +0.133 | +9.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 317 | +0.118 | -39.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 308 | +0.155 | +5.56€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 27 | +0.155 | +2.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 23 | +0.100 | -2.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 282 | +0.317 | +15.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 282 | +0.317 | +15.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 282 | +0.317 | +15.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 282 | +0.317 | +15.20€ | 0 | 0 |
| ✅ GBM_LATE_15M | 7061 | +0.097 | +2217.37€ | 0 | 5 |
| ✅ GBM_LATE_15M#15min | 7061 | +0.097 | +2217.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 1704 | +0.067 | +282.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1704 | +0.067 | +282.99€ | 0 | 2 |
| ✅ GBM_LATE_15M#ETH | 1592 | +0.073 | +279.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1592 | +0.073 | +279.73€ | 0 | 6 |
| ✅ GBM_LATE_15M#SOL | 1902 | +0.090 | +691.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1902 | +0.090 | +691.04€ | 1 | 3 |
| ✅ GBM_LATE_15M#XRP | 1863 | +0.150 | +963.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1863 | +0.150 | +963.61€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 4259 | +0.128 | +2191.67€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 4259 | +0.128 | +2191.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1094 | +0.087 | +401.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1094 | +0.087 | +401.81€ | 0 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1111 | +0.094 | +423.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1111 | +0.094 | +423.57€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1077 | +0.102 | +468.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1077 | +0.102 | +468.93€ | 0 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 977 | +0.239 | +897.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 977 | +0.239 | +897.36€ | 0 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 240 | +0.107 | +110.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 240 | +0.107 | +110.47€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 79 | -0.006 | +13.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 79 | -0.006 | +13.89€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 144 | +0.219 | +100.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 144 | +0.219 | +100.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 4264 | +0.083 | +1307.41€ | 0 | 5 |
| ✅ GBM_LATE_15M_TARDIO#15min | 4264 | +0.083 | +1307.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1026 | +0.043 | +149.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1026 | +0.043 | +149.92€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1028 | +0.033 | +94.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1028 | +0.033 | +94.57€ | 0 | 2 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 980 | +0.049 | +220.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 980 | +0.049 | +220.55€ | 1 | 3 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1230 | +0.183 | +842.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1230 | +0.183 | +842.37€ | 0 | 11 |
| ✅ GBM_LATE_5M | 328 | -0.021 | +7.05€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 328 | -0.021 | +7.05€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 51 | -0.066 | -9.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 51 | -0.066 | -9.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 48 | -0.080 | -0.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 48 | -0.080 | -0.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 75 | -0.162 | -1.01€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 75 | -0.162 | -1.01€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 154 | +0.083 | +18.00€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 154 | +0.083 | +18.00€ | 0 | 0 |
| ✅ GBM_LATE_60M | 336 | -0.112 | +4.40€ | 3 | 1 |
| ✅ GBM_LATE_60M#60min | 336 | -0.112 | +4.40€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 120 | -0.041 | +3.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 120 | -0.041 | +3.25€ | 4 | 1 |
| ✅ GBM_LATE_60M#ETH | 106 | -0.148 | -10.12€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 106 | -0.148 | -10.12€ | 4 | 0 |
| ✅ GBM_LATE_60M#SOL | 110 | -0.152 | +11.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 110 | -0.152 | +11.27€ | 5 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO | 9 | -0.143 | -2.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO#60min | 9 | -0.143 | -2.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 330 | -0.045 | -2.36€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 330 | -0.045 | -2.36€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 330 | -0.045 | -2.36€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 330 | -0.045 | -2.36€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 263 | +0.009 | +9.67€ | 2 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 263 | +0.009 | +9.67€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 263 | +0.009 | +9.67€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 263 | +0.009 | +9.67€ | 2 | 0 |
| ✅ ORDER_FLOW_5M | 1659 | +0.012 | +11.80€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1523 | +0.007 | -0.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 211 | +0.035 | +4.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 211 | +0.035 | +4.65€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 221 | -0.002 | -2.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 221 | -0.002 | -2.67€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 266 | -0.015 | -7.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 266 | -0.015 | -7.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 328 | +0.045 | +14.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 328 | +0.045 | +14.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 206 | -0.005 | -4.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 206 | -0.005 | -4.90€ | 1 | 0 |
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
| ✅ RESOLUTION_SNIPER | 11 | +0.190 | +3.49€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 11 | +0.190 | +3.49€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 267 | +0.084 | +32.81€ | 1 | 7 |
| ✅ STREAK_FADE_15M#15min | 267 | +0.084 | +32.81€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 58 | +0.050 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 58 | +0.050 | -0.08€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 86 | +0.136 | +24.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 86 | +0.136 | +24.51€ | 0 | 4 |
| ✅ STREAK_FADE_15M#XRP | 123 | +0.060 | +8.39€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 123 | +0.060 | +8.39€ | 0 | 4 |
| ✅ STREAK_FADE_5M | 246 | -0.048 | -24.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 246 | -0.048 | -24.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 47 | -0.153 | -8.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 3 | 0 |
| ✅ STREAK_FADE_5M#SOL | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 105 | -0.023 | -9.27€ | 0 | 0 |
| 🚫 STREAK_MOM_5M | 318 | -0.059 | -25.84€ | 4 | 0 |
| ✅ STREAK_MOM_5M#5min | 318 | -0.059 | -25.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 107 | -0.060 | -7.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 107 | -0.060 | -7.33€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 113 | -0.013 | -5.16€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 113 | -0.013 | -5.16€ | 2 | 0 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 5 | 0 |
| 🚫 STRUCT_NO_15M | 15 | -0.199 | -4.68€ | 0 | 0 |
| 🚫 STRUCT_NO_15M#15min | 15 | -0.199 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 2307 | +0.031 | +203.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2044 | +0.052 | +241.97€ | 0 | 3 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 130 | -0.061 | -11.21€ | 6 | 0 |
| ✅ UPDOWN_GBM#BNB | 226 | +0.070 | +51.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 226 | +0.070 | +51.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 531 | +0.052 | +63.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 447 | +0.088 | +78.44€ | 1 | 8 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 43 | -0.078 | -6.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 173 | +0.054 | +21.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 170 | +0.058 | +22.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 946 | +0.032 | +54.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 852 | +0.047 | +65.76€ | 0 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 55 | -0.026 | -3.07€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 202 | -0.073 | -13.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 133 | -0.048 | -6.67€ | 4 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 32 | -0.088 | -1.46€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 227 | +0.024 | +27.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 216 | +0.037 | +30.65€ | 4 | 0 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 130 | +0.288 | +23.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 130 | +0.288 | +23.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 61 | +0.278 | +9.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 61 | +0.278 | +9.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 69 | +0.289 | +14.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 69 | +0.289 | +14.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1339 | +0.165 | +619.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1339 | +0.165 | +619.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 132 | +0.209 | +80.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 132 | +0.209 | +80.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 152 | +0.136 | +33.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 152 | +0.136 | +33.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 130 | +0.227 | +93.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 130 | +0.227 | +93.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 264 | +0.150 | +83.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 264 | +0.150 | +83.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 324 | +0.104 | +93.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 324 | +0.104 | +93.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 337 | +0.202 | +234.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 337 | +0.202 | +234.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 11 | -0.021 | -0.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 11 | -0.021 | -0.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 11 | -0.021 | -0.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 11 | -0.021 | -0.76€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 336 | +0.180 | +67.16€ | 1 | 2 |
| ✅ WEEKLY_PRICE#BTC | 98 | +0.120 | -8.06€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 95 | +0.129 | -6.12€ | 0 | 2 |
| ✅ WEEKLY_PRICE#SOL | 143 | +0.252 | +81.34€ | 0 | 2 |