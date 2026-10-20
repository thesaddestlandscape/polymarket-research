import sys
sys.argv=[sys.argv[0],sys.argv[1] if len(sys.argv)>1 else 'BTC','x']+sys.argv[2:]
exec(open('/tmp/claude-0/-root-polymarket-research/06f7b0e2-eafc-4b79-84cd-46f932c672b1/scratchpad/agrega.py').read().split("if __name__=='__main__':")[0])
kind=sys.argv[3] if len(sys.argv)>3 else 'g'
def line(rs,tit):
    n=len(rs)
    if n==0: print(f'{tit:28s} n=0'); return
    days=len(set(r['day'] for r in rs))
    flag='' if n>=15 else ' [n<15 NO CONCLUYE]'
    cs={}
    for al in('lo','prop','hi'):
        vc=[(r['day'],)+cfill(r,al)[:2] for r in rs]; cs[al]=pooled(vc)
    vf=[(r['day'],)+feff(r,al)[:2] for r in rs] if False else None
    fe=pooled([(r['day'],)+feff(r,'prop')[:2] for r in rs])
    st=stats(rs)
    fs={al:fstar(rs,al)[0] for al in('lo','prop','hi')}
    h2={NAME[nm]:st[nm+'_h2'] for nm in VAR}
    print(f"{tit:28s} n={n:4d} d={days} c[lo/prop/hi]={cs['lo']:.2f}/{cs['prop']:.2f}/{cs['hi']:.2f} f_eff={fe:.2f} f*[lo/prop/hi]={fs['lo']}/{fs['prop']}/{fs['hi']} P(fill<=2s) opt/base/cons/prop={h2['opt']:.2f}/{h2['base']:.2f}/{h2['cons']:.2f}/{h2['prop']:.2f} any_full(prop)={st['rp_prop_full']:.2f}{flag}")
for c in coins:
    base=[r for r in rows if r['coin']==c and r.get('kind','g')==kind]
    print(f'##### {c} kind={kind} n={len(base)}')
    for t in TR:
        for b in ['0.10-0.15','0.15-0.20','0.20-0.25','0.25-0.30']:
            line([r for r in base if r['b']==b and r['tr']==t],f'{c} {t} {b}')
    print('-- por bucket (posterior)')
    for b in ['0.10-0.15','0.15-0.20','0.20-0.25','0.25-0.30']: line([r for r in base if r['b']==b],f'{c} {b}')
    print('-- por tramo (posterior)')
    for t in TR: line([r for r in base if r['tr']==t],f'{c} {t}')
    print('-- por dia (posterior)')
    for d in sorted(set(r['day'] for r in base)): line([r for r in base if r['day']==d],f'{c} dia {d}')
    print('-- coin total'); line(base,f'{c} TOTAL')
