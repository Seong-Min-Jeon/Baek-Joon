import sys
ip=sys.stdin.readline
a=int(ip())
l=[[0 for _ in range(a)] for _ in range(a)]
t=[[0 for _ in range(a)] for _ in range(a)]
for i in range(a):
    b=list(ip().strip())
    for j in range(a):
        l[i][j]=b[j]
        t[j][i]=b[j]
if(l==t):
    print('YES')
else:
    print('NO')