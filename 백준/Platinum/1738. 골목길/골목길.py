import sys
I=sys.stdin.readline
n,m=map(int,I().split())
l=[tuple(map(int,I().split())) for _ in range(m)]
r=[1e99 for _ in range(n+1)]
v=[0 for _ in range(n+1)]
r[1]=0
for i in range(n+1001):
    for j in range(m):
        x,y,c=l[j]
        c=-c
        if(r[x]!=1e99 and r[y]>r[x]+c):
            r[y]=r[x]+c
            v[y]=x
            if(i==n+1000 and y==n): print(-1); exit()
t=[]
q=n
while q!=0:
    t.append(q)
    q=v[q]
print(*reversed(t))