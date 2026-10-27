import sys
S=set(open(sys.argv[1],'rb').read().split())
o=sys.stdout.buffer
for l in sys.stdin.buffer:
    if (l[0]==113 or l[0]==116) and l[1]==44:
        p=l.split(b',',3)
        if len(p)>3 and p[2] in S: o.write(l)
