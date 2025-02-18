import sys
I=sys.stdin.readline
n,m=map(int,I().split())
l=[tuple(map(int,I().split())) for _ in range(m)]
r=[1e9 for _ in range(n+1)]
r[1]=0
for i in range(n):
    for j in range(m):
        x,y,c=l[j]
        if(r[x]!=1e9 and r[y]>r[x]+c):
            r[y]=r[x]+c
            if(i==n-1): print(-1); exit()
for i in range(2,n+1):
    if(r[i]==1e9): print(-1)
    else: print(r[i])