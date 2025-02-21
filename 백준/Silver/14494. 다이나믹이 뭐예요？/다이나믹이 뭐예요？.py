n,m=map(int,input().split())
l=[[1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if(i==0 or j==0): continue
        l[i][j]=(l[i-1][j]+l[i][j-1]+l[i-1][j-1])%(10**9+7)
print(l[-1][-1])