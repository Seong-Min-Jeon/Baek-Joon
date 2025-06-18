import sys
I=sys.stdin.readline
n,k=map(int,I().split())
l=[tuple(map(int,I().split())) for _ in range(k)]
d=[[0]*(n+1) for _ in range(k+1)]
for i in range(1,k+1):
    for j in range(1,n+1):
        if(l[i-1][1]<=j): d[i][j]=max(d[i-1][j],d[i-1][j-l[i-1][1]]+l[i-1][0])
        else: d[i][j]=d[i-1][j]
print(d[-1][-1])