import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m,q=F()
d={}
for _ in range(m):
    a,b,c=F()
    if(a>b): a,b=b,a
    d[(a,b)]=min(d.get((a,b),1e99),c)
for _ in range(q):
    s,e=F()
    if(s>e): s,e=e,s
    print(d.get((s,e),-1))