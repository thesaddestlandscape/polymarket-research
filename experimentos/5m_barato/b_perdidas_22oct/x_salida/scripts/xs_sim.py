# Simulador de reglas de salida a nivel de curva (PARTE B del PREREG). Importable (pasivo.py lo usa).
import numpy as np
H=12.0
REGLAS={'R0':dict(Bd=5,rat=1),'W2.5':dict(Bd=2.5,rat=1),'W3.5':dict(Bd=3.5,rat=1),'W8':dict(Bd=8,rat=1),'NR':dict(Bd=5,rat=0),
 'TPd3':dict(Bd=5,rat=1,tpd=3),'TPd6':dict(Bd=5,rat=1,tpd=6),'TPT3':dict(Bd=5,rat=1,tpt=3),'TPT6':dict(Bd=5,rat=1,tpt=6),
 'LOCK3_50':dict(Bd=5,rat=1,lock=(3,.5)),'LOCK6_50':dict(Bd=5,rat=1,lock=(6,.5)),'LOCK3_75':dict(Bd=5,rat=1,lock=(3,.75)),
 'MAXROT1':dict(Bd=5,rat=1,maxrot=1),'MAXROT2':dict(Bd=5,rat=1,maxrot=2),'TIME40':dict(Bd=5,rat=1,time40=40)}
def sim(flow,r,E_ini,minst=1.05,H=12.0):
    """flow: lista de (t, dayid, costs, pnls) ordenada por t. Devuelve dict de metricas."""
    Bd=r['Bd']; rat=r['rat']; tpd=r.get('tpd'); tpt=r.get('tpt'); lock=r.get('lock'); maxrot=r.get('maxrot'); t40=r.get('time40')
    E=E_ini; halted=E<H+Bd; active=not halted
    E0=E; F=E-Bd; P=0.0; pause=-1; day=None; Ed0=E; rot=0; cd=0; stopday=False
    takes=0; cost=0.0; Epk=E; dd=0.0; nb=0; Emin=E; tlast=None; tfirst=None
    for (t,dy,cs,ps) in flow:
        if halted: break
        if tfirst is None: tfirst=t
        tlast=t
        if dy!=day:
            day=dy; Ed0=E; rot=0; cd=0
            if stopday:
                stopday=False; active=False  # reanuda abajo
        if not active:
            if stopday or t<pause: nb+=len(cs); continue
            if E>=H+Bd: E0=E; F=E-Bd; P=0.0; active=True
            else: halted=True; break
        pend=0.0; got=0.0
        for c,pn in zip(cs,ps):
            if E-F-pend-c>=-1e-9: pend+=c; got+=pn; takes+=1; cost+=c
            else: nb+=1
        if pend==0.0: continue
        E+=got; cd+=1
        if E>Epk: Epk=E
        if Epk-E>dd: dd=Epk-E
        if E<Emin: Emin=E
        if rat and E-F>=Bd+1: F=E-Bd
        if E-E0>P: P=E-E0
        if lock and P>=lock[0]:
            f2=E0+lock[1]*P
            if f2>F: F=f2
        if tpt and E-E0>=tpt: active=False; pause=t+3600; continue
        if tpd and E-Ed0>=tpd: active=False; stopday=True; continue
        if t40 and cd>=t40: active=False; stopday=True; continue
        if E-F<minst:
            rot+=1
            if maxrot and rot>=maxrot: active=False; stopday=True
            elif E>=H+Bd: E0=E; F=E-Bd; P=0.0
            else: halted=True
    span=((tlast-tfirst)/86400.0) if tfirst is not None and tlast>tfirst else 1.0
    return dict(pnl=E-E_ini,takes=takes,cost=cost,dd=dd,halted=bool(halted),blocked=nb,Eend=E,span=span)
