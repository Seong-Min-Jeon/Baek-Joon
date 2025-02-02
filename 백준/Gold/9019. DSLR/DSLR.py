import sys
from collections import deque
I=sys.stdin.readline
for _ in range(int(I())):
    a,b=map(int,I().split())
    q=deque([(a,'')])
    v=[0 for _ in range(10000)]
    v[int(a)]=1
    while q:
        f=0
        n,m=q.popleft()
        d=(2*n%10000,'D')
        s=(n-1 if n>0 else 9999,'S')
        l=(n*10+n//1000-n//1000*10000,'L')
        r=(n//10+n%10*1000,'R')
        for e in (d,s,l,r):
            if(v[e[0]]==0):
                v[e[0]]=1
                q.append((e[0],m+e[1]))
                if(e[0]==b): print(m+e[1]); f=1; break
        if(f==1): break