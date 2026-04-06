f=lambda i,j,b,k:(d[i+1][j+k][b|(1<<j+k)]+d[i][j][b])%M
M=1000000000
n=int(input())
d=[[[0]*(1<<10) for _ in range(10)] for _ in range(n)]
for i in range(1,10):
    d[0][i][1<<i]=1
for i in range(n-1):
    for j in range(10):
        for b in range(1<<10):
            if(j==0): d[i+1][j+1][b|(1<<j+1)]=f(i,j,b,1)
            elif(j==9): d[i+1][j-1][b|(1<<j-1)]=f(i,j,b,-1)
            else: d[i+1][j+1][b|(1<<j+1)],d[i+1][j-1][b|(1<<j-1)]=f(i,j,b,1),f(i,j,b,-1)
r=0
for j in range(10):
    r+=d[-1][j][(1<<10)-1]
print(r%M)