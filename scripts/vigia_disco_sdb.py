#!/usr/bin/env python3
"""vigia_disco_sdb.py (27-Nov, PRIORIDAD 1 disco sdb, OK Javi). Alerta Telegram independiente de cualquier otro vigia si el volumen
/mnt/HC_Volume_106538179 baja de 15 GB libres (latch 6 h) o de 10 GB (libro_estado_ws PAUSA libro5/libro5_tx; latch 1 h).
Cron */10. Solo lectura (statvfs); estado fuera de git en /root/polymarket-research-datalogs/disco_27nov/vigia_estado.json."""
import json, os, shutil, sys, time
V = "/mnt/HC_Volume_106538179"
EST = "/root/polymarket-research-datalogs/disco_27nov/vigia_estado.json"
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    libre = shutil.disk_usage(V).free / 1e9
    try:
        est = json.load(open(EST))
    except (OSError, ValueError):
        est = {}
    ahora = time.time()
    # 28-Nov: nivel "urgente" <11 GB (ANTES de la pausa, cada hora) y aviso de recuperación al volver a >=15 GB.
    # Único vigía de disco sdb (el bloque duplicado de vigia_libro5tx_filas_hora.py se quitó).
    nivel = "critico" if libre < 10 else ("urgente" if libre < 11 else ("aviso" if libre < 15 else "ok"))
    latch = {"critico": 3600, "urgente": 3600, "aviso": 6 * 3600}.get(nivel)
    rango = {"aviso": 1, "urgente": 2, "critico": 3}
    escala = rango.get(nivel, 0) > rango.get(est.get("ult_aviso_nivel"), 0)      # subir de nivel avisa sin esperar al latch
    recupera = nivel == "ok" and est.get("ult_aviso_nivel") is not None
    enviar = recupera or (latch is not None and (escala or ahora - est.get("ult_aviso_ts", 0) >= latch))
    if enviar:
        if recupera:
            msg = f"✅ Volumen HC recuperado: {libre:.1f} GB libres (≥15 GB)."
        elif nivel == "critico":
            msg = f"🚨 Volumen HC con {libre:.1f} GB libres (<10): libro_estado_ws PAUSA libro5/libro5_tx; cada dia sin cobertura retrasa la mirada de B. Liberar espacio YA."
        elif nivel == "urgente":
            msg = f"🚨 URGENTE volumen HC con {libre:.1f} GB libres (<11): a <10 GB libro_estado_ws PAUSA libro5/libro5_tx. Liberar ahora."
        else:
            msg = f"⚠️ Volumen HC con {libre:.1f} GB libres (<15 GB). A <10 GB se pausa libro5/libro5_tx."
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram(msg, bot="cripto")
            est["ult_aviso_ts"], est["ult_aviso_nivel"] = (0, None) if recupera else (ahora, nivel)
        except Exception as e:
            print(f"telegram fallo: {type(e).__name__}: {e}", file=sys.stderr)
            return 1
    est.update({"libre_gb": round(libre, 1), "nivel": nivel, "ts": int(ahora)})
    tmp = EST + ".tmp"
    json.dump(est, open(tmp, "w"))
    os.replace(tmp, EST)
    print(json.dumps({"libre_gb": est["libre_gb"], "nivel": nivel, "enviado": enviar}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
