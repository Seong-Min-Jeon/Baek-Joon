from collections import defaultdict as D
I=input
n,m=map(int,I().split())
l=[*map(int,I().split())]
d=D(int)
z=1e99
for _ in range(m):
    t=I().strip().split()
    k=int(t.pop(0))
    z=min(z,k)
    for i,e in enumerate(t):
        if(e=='O'):
            d[k]+=l[i]
a,b=z,0
for k in d:
    if(b<d[k]): a,b=k,d[k]
    elif(b==d[k]): a=min(a,k)
print(a,b)