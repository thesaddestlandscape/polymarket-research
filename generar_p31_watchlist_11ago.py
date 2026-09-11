"""P31 (11-Ago): genera la watchlist FIJA de wallets candidatas (fade/follow)
a partir de data/shadow/p31_splithalf_wallets.json (robustas, mismo signo
en split-half, ya TWAP-limpio) -- se ejecuta UNA VEZ para fijar el corte
in-sample/forward. NO se re-genera automáticamente (si se quisiera ampliar
la watchlist con nuevas wallets, es una decisión explícita nueva, no un
cron que se reescriba solo -- así el forward test es limpio, sin mover la
portería).

vigia_p31_wallets_forward.py consume esta watchlist y mide SOLO datos con
ts_trade > cutoff_utc, out-of-sample de verdad respecto al análisis de
hoy (11-Ago).
"""
import json
from collections import defaultdict
from datetime import datetime, timezone

OUT = "data/shadow/p31_wallets_watchlist.json"
MIN_WALLETS_POR_COMBO = 2  # mismo umbral que el barrido pooled de hoy

d = json.load(open("data/shadow/p31_splithalf_wallets.json"))
robustos = [v for v in d.values() if v["mismo_signo"]]

grupos = defaultdict(lambda: {"fade": [], "follow": []})
for v in robustos:
    key = (v["activo"], v["marco"])
    lado = "fade" if v["edge2_pp"] < 0 else "follow"
    grupos[key][lado].append(v["wallet"])

combos = {}
for (activo, marco), g in grupos.items():
    for lado in ("fade", "follow"):
        wallets = sorted(set(g[lado]))
        if len(wallets) >= MIN_WALLETS_POR_COMBO:
            combos[f"{activo}#{marco}#{lado}"] = {
                "activo": activo, "marco": marco, "lado": lado,
                "wallets": wallets, "n_wallets": len(wallets),
            }

watchlist = {
    "cutoff_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "origen": "idea_p31_fade_wallets_sistematicamente_malas_11ago -- split-half + gate pooled 11-Ago",
    "combos": combos,
}

with open(OUT, "w") as f:
    json.dump(watchlist, f, indent=1)

print(f"Watchlist: {len(combos)} combos, cutoff={watchlist['cutoff_utc']}")
for k, v in combos.items():
    print(f"  {k}: {v['n_wallets']} wallets")
