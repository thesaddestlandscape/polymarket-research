import json, sys, numpy as np, pandas as pd
H='/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/'
OWN='0x659a40ff9920febc5a66836213040924343d297f'
def parse(inp):
    b=bytes.fromhex(inp[10:]); w=lambda i:int.from_bytes(b[i:i+32],'big')
    off_t,off_m,tfill,off_f=w(32),w(64),w(96),w(128)
    def order(s):
        f=[w(s+32*k) for k in range(12)]
        return dict(maker='0x'+f[1].to_bytes(32,'big')[12:].hex(),tokenId=str(f[3]),mA=f[4],tA=f[5],side=f[6],ts=f[8])
    to=order(off_t); n=w(off_m); mk=[order(off_m+32+w(off_m+32*(1+i))) for i in range(n)]
    nf=w(off_f); fl=[w(off_f+32*(1+i)) for i in range(nf)]
    return to,mk,fl,tfill
CD={}
for f in ('/root/polymarket-research-datalogs/cola_posicion/calldata_b.jsonl',H+'calldata_extra.jsonl'):
    for l in open(f): d=json.loads(l); CD[d['tx']]=d['input']
T=pd.read_pickle(H+'tomador_202.pkl'); rows=[]
for r in T.itertuples():
    inp=CD.get(r.tx)
    if inp is None or not inp.startswith('0x3c2b4399'): continue
    to,mk,fl,tf=parse(inp); tok=str(r.tok); own=[o for o in mk if o['maker']==OWN and o['tokenId']==tok]
    if not own: continue
    o=own[0]; side=to['side']
    # precio del tomador (siempre USDC/accion): BUY mA=USDC,tA=acc ; SELL mA=acc,tA=USDC
    px_t = to['mA']/to['tA'] if side==0 else to['tA']/to['mA']
    acc_t = (to['tA'] if side==0 else to['mA'])/1e6          # acciones del tomador
    usd_t = (to['mA'] if side==0 else to['tA'])/1e6
    fill_unit_acc = tf/1e6 if side==1 else tf/1e6/px_t      # takerFillAmount esta en la unidad makerAmount del tomador (SELL: acciones; BUY: USDC)
    own_acc=(o['mA'] if o['side']==1 else o['tA'])/1e6       # nuestra orden: SELL->mA acciones ; BUY->tA acciones
    rows.append(dict(oid=r.oid,side_tk=side,px_t=px_t,acc_t=acc_t,usd_t=usd_t,fill_acc=fill_unit_acc,own_acc=own_acc,tk_sz=r.tk_sz,tk_rem=r.tk_rem,own_sh_tx=r.own_sh_tx,rem_acc=(1-fill_unit_acc/acc_t)))
X=pd.DataFrame(rows); print(len(X),'de',len(T))
print('side_tk',X.side_tk.value_counts().to_dict())
print('px_t en (0,1):',bool(((X.px_t>0)&(X.px_t<1)).all()), 'min/max',X.px_t.min(),X.px_t.max())
print('tk_sz == acciones del tomador (acc_t):',bool((X.tk_sz-X.acc_t).abs().max()<1e-9),' max|dif|',(X.tk_sz-X.acc_t).abs().max())
print('tk_sz*px_t == USDC del tomador:',float((X.tk_sz*X.px_t-X.usd_t).abs().max()))
print('tk_rem es fraccion [0,1]:',float(X.tk_rem.min()),float(X.tk_rem.max()),' tk_rem == rem en acciones:',float((X.tk_rem-X.rem_acc).abs().max()))
print('fill_acc>=own_acc-eps (lo casado cubre lo nuestro):',float((X.fill_acc-X.own_acc).min()))
print('own_sh_tx == acciones propias on-chain (own_acc):',float((X.own_sh_tx-X.own_acc).abs().max()))
print(X[['side_tk','px_t','acc_t','usd_t','fill_acc','own_acc','tk_rem']].head(6).round(4).to_string())
