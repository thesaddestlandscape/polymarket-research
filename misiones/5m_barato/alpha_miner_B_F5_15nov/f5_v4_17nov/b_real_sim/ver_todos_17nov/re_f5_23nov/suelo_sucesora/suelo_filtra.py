#!/usr/bin/env python3
"""suelo_filtra.py DIA_HASTA -- (E2) de la tabla regenerada por suelo_tabla.py (tabla_suelo_ventanas_19nov.csv, todos los h_*.done) saca dia>=18-Nov y <=DIA_HASTA a tabla_suelo_sucesora_18_<DD>nov.csv (+ .sha256), y comprueba:
(1) filas = 288*6 por dia (BNB,BTC,DOGE,ETH,SOL,XRP); (2) el 17-Nov regenerado es IDENTICO al firmado (cierre_limites_19nov/tabla_suelo_ventanas_19nov.csv); (3) si DIA_HASTA >= 22-Nov, las filas <=22-Nov reproducen el sha firmado b72d49fa... Escribe PROPUESTA_TABLA_SUELO_<DIA_HASTA>.json (ruta+sha) para la firma del chief. 0 datos de EV."""
import sys, os, json, hashlib, csv
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
FIRMADA = HERE + '../../cierre_limites_19nov/tabla_suelo_ventanas_19nov.csv'; SHA_18_22 = 'b72d49faa846f270460bc8a4eb9fe82850ec58f1c335fc00c3ae1b9090300919'
def sha_b(b): return hashlib.sha256(b).hexdigest()
def main(hasta):
    rows = open(HERE + 'tabla_suelo_ventanas_19nov.csv').read().split('\n'); hdr = rows[0]; body = [r for r in rows[1:] if r]
    sel = [r for r in body if '2026-11-18' <= r[:10] <= hasta]; dias = sorted({r[:10] for r in sel}); esperado = 288 * 6 * len(dias)
    ok = dict(filas=len(sel), dias=dias, filas_esperadas=esperado, filas_ok=(len(sel) == esperado and len(dias) == int(hasta[8:]) - 17))
    fir = [r for r in open(FIRMADA).read().split('\n')[1:] if r and r[:10] == '2026-11-17']; reg17 = [r for r in body if r[:10] == '2026-11-17']
    ok['17nov_identico_a_la_firmada'] = (fir == reg17 and len(fir) == 1728)
    if hasta >= '2026-11-22':
        b22 = (hdr + '\n' + '\n'.join(r for r in sel if r[:10] <= '2026-11-22') + '\n').encode(); ok['reproduce_18_22_firmada'] = (sha_b(b22) == SHA_18_22)
    out = HERE + f'tabla_suelo_sucesora_18_{hasta[8:]}nov.csv'; data = (hdr + '\n' + '\n'.join(sel) + '\n').encode()
    open(out + '.tmp', 'wb').write(data); os.replace(out + '.tmp', out); s = sha_b(data); open(out.replace('.csv', '.sha256'), 'w').write(s + '  ' + os.path.basename(out) + '\n')
    prop = dict(ruta=out, sha256=s, dias=f'2026-11-18..{hasta}', comprobaciones=ok, estado='PROPUESTA_PARA_FIRMA_CHIEF (anadir a rf5_cortes.json::tabla_suelo_sucesora antes de abrir el dia)')
    json.dump(prop, open(HERE + f'PROPUESTA_TABLA_SUELO_{hasta}.json', 'w'), indent=1); print(json.dumps(prop)); return 0 if (ok['filas_ok'] and ok['17nov_identico_a_la_firmada'] and ok.get('reproduce_18_22_firmada', True)) else 2
if __name__ == '__main__': sys.exit(main(sys.argv[1]))
