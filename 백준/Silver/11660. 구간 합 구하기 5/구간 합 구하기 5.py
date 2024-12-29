import sys
ip=sys.stdin.readline
n,m=map(int,ip().split())
l=[list(map(int,ip().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(i==0 and j==0): pass
        elif(i==0): l[i][j]+=l[i][j-1]
        elif(j==0): l[i][j]+=l[i-1][j]
        else: l[i][j]+=l[i-1][j]+l[i][j-1]-l[i-1][j-1]
for _ in range(m):
    a,b,x,y=map(int,ip().split())
    if(a==1 and b==1): print(l[x-1][y-1])
    elif(a==1): print(l[x-1][y-1]-l[x-1][b-2])
    elif(b==1): print(l[x-1][y-1]-l[a-2][y-1])
    else: print(l[x-1][y-1]-l[x-1][b-2]-l[a-2][y-1]+l[a-2][b-2])