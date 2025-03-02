import sys
I=sys.stdin.readline
t,w=map(int,I().split())
l=[int(I()) for _ in range(t)]
r=[[0 for _ in range(t)] for _ in range(w+1)]
for i in range(t):
    if(l[i]==2): r[0][i]=r[0][i-1]
    else: r[0][i]=r[0][i-1]+1
for i in range(1,w+1):
    p=1
    for j in range(t):
        if(j==0): r[i][j]=1; p=l[j]; continue
        if(p==l[j]): r[i][j]=r[i][j-1]+1
        else: 
            m=0
            for k in range(j):
                if(l[k]==l[j]): m=max(m,r[i][k])
            r[i][j]=max(r[i-1][j-1]+1,m+1); p=l[j]
print(max(r[-1]))