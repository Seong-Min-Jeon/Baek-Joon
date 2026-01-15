I=input
F=lambda:map(int,I().split())
n,m=F()
l=[list(F()) for _ in range(n)]
r=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if(l[i][j]==0):
            if(i==0 or j==0): r[i][j]=1
            else: r[i][j]=min(r[i-1][j],r[i][j-1],r[i-1][j-1])+1
print(max(map(max,r)))