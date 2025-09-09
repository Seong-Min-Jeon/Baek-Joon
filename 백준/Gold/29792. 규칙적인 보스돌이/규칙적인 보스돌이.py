import math
n,m,k=map(int,input().split())
p=[int(input()) for _ in range(n)]
l=[tuple(map(int,input().split())) for _ in range(k)]
p.sort()
p=p[n-m:n+1]
r=[[0]*901 for _ in range(m)]
for v,d in enumerate(p):
    for i in range(k):
        h,c=l[i]
        for j in range(900,math.ceil(h/d)-1,-1):
            r[v][j]=max(r[v][j],r[v][j-math.ceil(h/d)]+c)
print(sum([max(r[i]) for i in range(m)]))