#!/usr/bin/env python3
"""f11: PnL por dia 24-Sep..04-Oct SIN sesgo de supervivencia: TRADE de /activity + desenlace oficial gamma (condition_ids, closed=true). Unido a ledger on-chain 05-23 Oct."""
import json, time, requests, pandas as pd, numpy as np
O = "/root/polymarket-research-datalogs/wallet_pspspsps5/"
A = pd.read_csv(O + "actividad.csv.gz"); T = A[A.type == "TRADE"].copy()
T["ts_c"] = T.slug.str.extract(r"-(\d{10})$")[0].astype(float) + 300
T = T[T.slug.str.contains("-updown-5m-")]
T["dia"] = pd.to_datetime(T.ts_c, unit="s").dt.strftime("%Y-%m-%d")
print("trades", len(T), "mercados", T.conditionId.nunique(), "sides", T.side.value_counts().to_dict())
cids = sorted(T.conditionId.unique()); win = {}; s = requests.Session()
for k in range(0, len(cids), 40):
    for a in range(4):
        try:
            r = s.get("https://gamma-api.polymarket.com/markets", params=[("condition_ids", c) for c in cids[k:k + 40]] + [("closed", "true"), ("limit", "40")], timeout=30)
            if r.status_code == 200: break
        except Exception: pass
        time.sleep(2)
    for m in r.json() or []:
        pr = m.get("outcomePrices"); pr = json.loads(pr) if isinstance(pr, str) else pr
        oc = m.get("outcomes"); oc = json.loads(oc) if isinstance(oc, str) else oc
        if pr and max(map(float, pr)) >= .999: win[m["conditionId"]] = oc[int(np.argmax(list(map(float, pr))))]
print("desenlace oficial", len(win), "de", len(cids))
T["w"] = T.conditionId.map(win); T = T[T.w.notna()]
T["pnl"] = np.where(T.side == "BUY", np.where(T.outcome == T.w, T["size"], 0) - T.usdcSize, T.usdcSize - np.where(T.outcome == T.w, T["size"], 0))
T["cost"] = np.where(T.side == "BUY", T.usdcSize, 0)
d = T.groupby("dia").agg(pnl=("pnl", "sum"), c=("cost", "sum"), n=("pnl", "size"))
d.to_csv(O + "dia_api_sep_oct.csv")
print(d.round(0).to_string())
U = pd.read_csv(O + "units.csv.gz", dtype={"mkt": str}); u = U.assign(c=U.cost + U.fee).groupby("dia").agg(pnl=("pnl", "sum"), c=("c", "sum"))
dd = pd.concat([d.loc["2026-09-24":"2026-10-04", ["pnl", "c"]], u.loc["2026-10-05":"2026-10-23"]])
print("\n30 dias 24-Sep..23-Oct: PnL %.0f coste %.0f EV %.4f verdes %d/%d ; sin 2 mejores dias %.0f ; sin 5 mejores %.0f ; mejor dia %.0f peor %.0f" % (dd.pnl.sum(), dd.c.sum(), dd.pnl.sum() / dd.c.sum(), (dd.pnl > 0).sum(), len(dd), dd.pnl.sort_values().iloc[:-2].sum(), dd.pnl.sort_values().iloc[:-5].sum(), dd.pnl.max(), dd.pnl.min()))
x = dd.loc["2026-09-24":"2026-10-04"]; print("24-Sep..04-Oct: PnL %.0f verdes %d/%d EV %.4f" % (x.pnl.sum(), (x.pnl > 0).sum(), len(x), x.pnl.sum() / x.c.sum()))
# validacion del metodo API sobre el solape 05-07 Oct
print("solape 05-06 Oct (API vs ledger):", d.loc["2026-10-05":"2026-10-06", "pnl"].round(0).to_dict(), u.loc["2026-10-05":"2026-10-06", "pnl"].round(0).to_dict())
