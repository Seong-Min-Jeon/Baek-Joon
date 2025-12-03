import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m=F()
l=[[1e99]*n for _ in range(n)]
for i in range(n-1):
    l[i][i]=0
    for j,e in enumerate(F()):
        l[i][i+j+1]=e
        l[i+j+1][i]=e
l[-1][-1]=0
for k in range(n):
    for i in range(n):
        for j in range(i,n):
            if(i==k or j==k): continue
            if(l[i][j]>=l[i][k]+l[k][j]):
                l[i][j]=1e99
q=[]
for i in range(n):
    for j in range(i,n):
        if(i==j or l[i][j]>500): continue
        q.append([i+1,j+1,l[i][j]])
if(m<len(q)): print(0); exit()
print(1)
for i in range(m):
    if(i<len(q)): print(*q[i])
    else: print(*q[-1])