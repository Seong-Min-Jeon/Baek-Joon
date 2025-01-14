import sys
I=sys.stdin.readline
n=int(I())
l=[list(map(int,I().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if(l[i][k]+l[k][j]==2): l[i][j]=1
for e in l: print(' '.join(map(str,e)))