import sys
I=sys.stdin.readline
n,m=map(int,I().split())
l=[0]*(n+1)
for _ in range(m):
    q,i,*v=map(int,I().split())
    if(q==1): l[i]=l[i]|(1<<v[0])
    elif(q==2): l[i]=l[i]&~(1<<v[0])
    elif(q==3): l[i]=l[i]&~(1<<20); l[i]=l[i]<<1
    else: l[i]=l[i]&~(1<<1); l[i]=l[i]>>1
del l[0]
print(len(set(l)))