# ADENDA_V2V3_rf5 (28-Nov-2026) -- consumidores on-chain de RF5 sobre cadena_v2v3. NO FIRMADA (la firma el chief). Los ficheros sellados de re_f5_23nov/ (HASHES_rf5.txt y todo lo que lista) NO se han tocado.

## 1. Alcance
Los consumidores on-chain de rf5 (`cobertura_bruta.py`, `vigia_rf5.py`) leen solo `onchain_fills_{x}.csv.gz` (V2, contrato 0xe111...), ciego a SOL/XRP/BNB/DOGE/HYPE desde ~24-Nov (Protocol V2 por mercado). Esta adenda NO los edita: añade dos WRAPPERS nuevos que importan los modulos sellados SIN modificarlos y sustituyen solo la fuente de ficheros.
- `cobertura_bruta_v2v3.py`: `prepara_keep` crea un directorio `keep` de symlinks: dias <=22-Nov = EXACTAMENTE los mismos ficheros que el sellado (incluidos `_parcial`); dias >=23-Nov = `cadena_v2v3.rutas_cadena` (V2) + `onchain_fills_{x}_v3.csv.gz` (V3 OBLIGATORIO). Escribe en `out_rf5_ciego_v2v3/`; el JSON lleva el bloque `adenda_v2v3` {sha16_cadena_v2v3, sha16_wrapper, versiones, ficheros}.
- `vigia_rf5_v2v3.py`: monkeypatch de `resumen_texto`/`avisos` del sellado; alerta R11 (cadena no COMPLETE por moneda). `estado_cadena(d, ruta=None)`.
- `cadena_v2v3.py` (en exp5bis_27nov/): estado POR MONEDA; COMPLETE solo si V2 y V3 (>=23-Nov) completos para ESA moneda. Un dia de una moneda sin cadena => excluido (nunca 0).

## 2. Identidad (condicion de cierre)
Para todo dia <=22-Nov el resultado del wrapper debe ser bit a bit el del sellado (`cobertura_bruta_v2v3.py --identidad DIA` compara con out_rf5_ciego/cobertura_bruta_x.json). Estado a la firma de esta adenda: 7 dias (15-19, 21, 22-Nov) identicos, 20-Nov no testable (IDENTIDAD_V2V3_28nov.txt). Los dias 21 y 22-Nov (fin de semana) se etiquetan **«baja potencia»**: su identidad es valida pero aportan poca muestra (no son evidencia de potencia para ningun gate); 18 y 19-Nov se relanzaron el 28-Nov con log (`paso3/ident_v2v3_18_19_rerun.log`); sin identidad OK => wrapper NO consumible.

## 3. Lo que NO cambia
Criterios, cortes (rf5_cortes.json), gates, semilla, motor y sellos: los de HASHES_rf5.txt. La adenda no re-ejecuta ni reinterpreta ningun veredicto; solo habilita que los dias >=23-Nov de SOL/XRP (y futuros V2) entren con cadena completa.

## 4. Hashes
`HASHES_rf5_adenda_v2v3.txt` (sha256 de cadena_v2v3.py y los dos wrappers). Verificar: `sha256sum -c HASHES_rf5_adenda_v2v3.txt` desde re_f5_23nov/ (rutas absolutas).
