import sys
I=sys.stdin.readline
n=int(I())
l=[list(map(int,I().split())) for _ in range(n)]
r=[[1e9 for _ in range(n)] for _ in range(n)]
for c in range(n):
    for i in range(n-c):
        r[i][i]=0
        j=i+c
        for k in range(i,j):
            r[i][j]=min(r[i][j],r[i][k]+r[k+1][j]+l[i][0]*l[k][1]*l[j][1])
print(r[0][-1])