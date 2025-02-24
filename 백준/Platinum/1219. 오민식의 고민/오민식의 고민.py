import sys
I=sys.stdin.readline
n,s,d,m=map(int,I().split())
l=[list(map(int,I().split())) for _ in range(m)]
e=list(map(int,I().split()))
for i in range(m): l[i][2]-=e[l[i][1]]
r=[1e9 for _ in range(n)]
r[s]=-e[s]
q=[]
for i in range(n):
    for j in range(m):
        x,y,c=l[j]
        if(r[x]!=1e9 and r[y]>r[x]+c):
            r[y]=r[x]+c
            if(i==n-1): q.append(y)
v=[0 for _ in range(n)]
while q:
    p=q.pop(0)
    for x,y,c in l:
        if(p==x and v[y]==0): 
            if(y==d): print('Gee'); exit()
            q.append(y)
            v[y]=1
if(r[d]==1e9): print('gg')
else: print(-r[d])