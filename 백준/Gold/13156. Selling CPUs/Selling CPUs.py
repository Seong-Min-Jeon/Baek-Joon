c,m=map(int,input().split())
l=[[0]+[*map(int,input().split())] for _ in range(m)]
r=[[0]*(c+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,c+1):
        for k in range(j+1):
            r[i][j]=max(r[i][j],r[i-1][j-k]+l[i-1][k])
print(r[-1][-1])