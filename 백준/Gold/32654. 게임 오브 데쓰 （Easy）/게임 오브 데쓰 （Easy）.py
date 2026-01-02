import sys
I=sys.stdin.readline
n=int(I())
l=[[] for _ in range(n+1)]
for i in range(n):
    a,b=map(int,I().split())
    l[i+1].append(a)
    l[i+1].append(b)
d=[[0]*99 for _ in range(n+1)]
d[l[1][0]][0]=1
d[l[1][1]][0]=1
for k in range(98):
    for i in range(n+1):
        if(d[i][k]==1):
            d[l[i][0]][k+1]=1
            d[l[i][1]][k+1]=1
for k in range(9,99):
    if(d[1][k]==0): print(k+1); exit()
print(-1)