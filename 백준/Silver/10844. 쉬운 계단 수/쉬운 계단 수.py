f=lambda i,j,k:(d[i+1][j+k]+d[i][j])%M
M=1000000000
n=int(input())
d=[[0]*10 for _ in range(n)]
d[0]=[0]+[1]*9
for i in range(n-1):
    for j in range(10):
        if(j==0): d[i+1][j+1]=f(i,j,1)
        elif(j==9): d[i+1][j-1]=f(i,j,-1)
        else: d[i+1][j+1],d[i+1][j-1]=f(i,j,1),f(i,j,-1)
print(sum(d[-1])%M)