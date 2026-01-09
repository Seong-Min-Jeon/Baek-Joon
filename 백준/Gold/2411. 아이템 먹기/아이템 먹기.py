import sys
I=sys.stdin.readline
n,m,a,b=map(int,I().split())
l=[[(0,0)]*m for _ in range(n)]
l[0][0]=(1,0)
s,v=set(),set()
for _ in range(a):
    x,y=map(int,I().split())
    s.add((x-1,y-1))
for _ in range(b):
    x,y=map(int,I().split())
    v.add((x-1,y-1))
for i in range(n):
    for j in range(m):
        f=(i,j) in s
        if((i,j) in v): continue
        if(i==0 and j==0): continue
        if(j==0 or l[i-1][j][1]>l[i][j-1][1]): l[i][j]=(l[i-1][j][0],l[i-1][j][1]+f)
        elif(i==0 or l[i-1][j][1]<l[i][j-1][1]): l[i][j]=(l[i][j-1][0],l[i][j-1][1]+f)
        else: l[i][j]=(l[i-1][j][0]+l[i][j-1][0],l[i-1][j][1]+f)
print(l[-1][-1][0])