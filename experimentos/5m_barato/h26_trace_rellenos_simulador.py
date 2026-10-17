"""Diagnóstico H26: re-ejecuta UN día del simulador (solo JOIN C0 CONS+OPT, SH=5) importando el módulo SIN modificarlo y registra
cada relleno simulado y cada segmento de orden (alta, cancelación efectiva, precio, cola). Solo lectura; no escribe cachés del simulador."""
import sys, gzip, json, time, pickle
sys.path.insert(0,"/root/polymarket-research")
import analisis_5m_maker_banda_simulador as S
d=sys.argv[1]
eng=S.construir_motores(("JOIN",),("CONS","OPT"),(),{"C0"},placebo=False)
print([e.nombre for e in eng])
fills=[]; segs=[]
orig_t=S.Motor.t; orig_cuenta=S.Motor._cuenta
def t_wrap(self,tk,p,side,sz,t_ex,t_rx):
    vv=self.vivos.get(tk if side=="SELL" else self.par.get(tk))
    antes={}
    if vv:
        for pos in vv:
            antes[id(pos)]=(pos,pos.lleno,[ (g,g.lleno) for g in pos.segs])
    orig_t(self,tk,p,side,sz,t_ex,t_rx)
    for k,(pos,l0,gs) in antes.items():
        for g,gl0 in gs:
            if g.lleno>gl0+1e-9:
                m=pos.meta
                fills.append((pos.e.nombre,m.coin,m.mkt,m.lado,t_ex,m.fin,g.precio,g.lleno-gl0,p,side,sz,g.cola,g.adv,g.act,g.ceff))
S.Motor.t=t_wrap
def cuenta_wrap(self,pos,seg):
    if not seg.cont:
        m=pos.meta
        segs.append((pos.e.nombre,m.coin,m.mkt,m.lado,seg.precio,seg.act,seg.ceff,seg.cola,seg.adv,seg.lleno,seg.qty,seg.dec))
    orig_cuenta(self,pos,seg)
S.Motor._cuenta=cuenta_wrap
t0=time.time()
dia_ini=int(S.datetime.fromisoformat(d+"T00:00:00+00:00").timestamp()*1000)
ext=S.Externas()  # sin Binance ni 15m: C0 no los usa
mo=S.procesar_registro(S.VOL/"m5_registro"/f"m5_registro_{d}.csv.gz",ext,eng,dia_ini)
print("lineas",mo.st["lineas"],"tramos",len(mo.tramos),"fills",len(fills),"segs",len(segs),"seg",time.time()-t0)
filas=mo.filas(d)
pickle.dump(dict(fills=fills,segs=segs,filas=filas,tramos=mo.tramos),open(f"trace_{d}.pkl","wb"))
