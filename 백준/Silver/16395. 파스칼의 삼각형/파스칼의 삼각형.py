n,k=map(int,input().split())
l=[[] for _ in range(n+1)]
for i in range(n+1):
    for j in range(i):
        if(j==0 or j==i-1): l[i].append(1)
        else: l[i].append(l[i-1][j-1]+l[i-1][j])
print(l[n][k-1])