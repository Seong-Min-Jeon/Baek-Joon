import sys
I=sys.stdin.readline
n,m=map(int,I().split())
l=[0b0]*(n+1)
for _ in range(m):
    t=[*map(int,I().split())]
    if(len(t)==3):
        q,i,v=t
        if(q==1): l[i]=l[i]|(1<<v)
        else: l[i]=l[i]&~(1<<v)
    else:
        q,i=t
        if(q==3): l[i]=l[i]&~(1<<20); l[i]=l[i]<<1
        else: l[i]=l[i]&~(1<<1); l[i]=l[i]>>1
del l[0]
print(len(set(l)))