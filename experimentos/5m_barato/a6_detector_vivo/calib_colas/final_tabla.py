import sys,os,json
coinsl=sys.argv[1].split(','); tag=sys.argv[2] if len(sys.argv)>2 else ''
src=open('/root/polymarket-research/experimentos/5m_barato/a6_detector_vivo/calib_colas/agrega.py').read().split("if __name__=='__main__':")[0]
src=src.replace("sys.argv[1].split(',')",repr(coinsl)).replace("muestras_{c}.ndjson","muestras_{c}"+tag+".ndjson")
exec(src)
rows=[r for r in rows if r.get('kind','g')=='g']
def nearest(f):
    return min((abs(f-0.0),'opt'),(abs(f-0.5),'base'),(abs(f-1.0),'cons'))[1]
out=[]
def cc(rs,al):
    return pooled([(r['day'],)+cfill(r,al)[:2] for r in rs])
for c in coinsl:
    base=[r for r in rows if r['coin']==c]
    if not base: continue
    out.append(f'##### {c} n={len(base)} mercados={len(set(r["mkt"] for r in base))}')
    out.append('tramo bucket n c_lo/prop/hi f*_hi/prop/lo P(fill<=2s)opt/base/cons/prop')
    for t in TR:
        for b in ['0.10-0.15','0.15-0.20','0.20-0.25','0.25-0.30']:
            rs=[r for r in base if r['tr']==t and r['b']==b]
            if not rs: out.append(f'{t} {b} n=0'); continue
            if len(rs)<15: out.append(f'{t} {b} n={len(rs)} [n<15 NO CONCLUYE]'); continue
            st=stats(rs)
            out.append(f"{t} {b} n={len(rs)} c={cc(rs,'lo'):.2f}/{cc(rs,'prop'):.2f}/{cc(rs,'hi'):.2f} f*={fstar(rs,'hi')[0]}/{fstar(rs,'prop')[0]}/{fstar(rs,'lo')[0]} P2s={st['sh_f000_h2']:.2f}/{st['sh_f050_h2']:.2f}/{st['sh_f100_h2']:.2f}/{st['rp_prop_h2']:.2f}")
    st=stats(base)
    cis={al:dayci([(r['day'],)+cfill(r,al)[:2] for r in base]) for al in('lo','prop','hi')}
    fd={al:fstar_dias(base,al) for al in('lo','prop','hi')}
    fs={al:fstar(base,al)[0] for al in('lo','prop','hi')}
    fe=pooled([(r['day'],)+feff(r,'prop')[:2] for r in base])
    d3={k:sum(abs(x-y) for x,y in zip(pcurve(base,'rp_prop'),pcurve(base,k)))/12 for k in('sh_f000','sh_f050','sh_f100')}
    out.append(f"TOTAL {c}: dias={len(set(r['day'] for r in base))} fill_final(prop)={st['rp_prop_any']:.2f} opt/base/cons={st['sh_f000_any']:.2f}/{st['sh_f050_any']:.2f}/{st['sh_f100_any']:.2f}")
    for al in('lo','prop','hi'):
        ci=cis[al]; out.append(f"  c[{al}]={ci[0]:.3f} IC90dias=({ci[1]:.3f},{ci[2]:.3f})" if ci and ci[1] is not None else f"  c[{al}]={ci}")
    out.append(f"  f_eff(vol)={fe:.3f}  f*(hi/prop/lo)={fs['hi']}/{fs['prop']}/{fs['lo']}  f*dias(prop)={fd['prop']}  dist prop->opt/base/cons={d3['sh_f000']:.3f}/{d3['sh_f050']:.3f}/{d3['sh_f100']:.3f}")
    best=min(d3,key=d3.get)
    out.append(f"  COLA recomendada (min dist vs prop)={ {'sh_f000':'opt','sh_f050':'base','sh_f100':'cons'}[best]}; rango por reparto: {nearest(fs['hi'])}..{nearest(fs['lo'])} (f* {fs['hi']}-{fs['lo']})")
open('/root/polymarket-research/experimentos/5m_barato/a6_detector_vivo/calib_colas/tabla_monedas'+tag+'.txt','w').write('\n'.join(out)+'\n')
print('\n'.join(l for l in out if l.startswith('#####') or l.startswith('TOTAL') or l.startswith('  c[') or l.startswith('  f_eff') or l.startswith('  COLA')))
