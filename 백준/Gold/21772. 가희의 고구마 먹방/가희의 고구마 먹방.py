import sys
import time

def move(x,y,t,g,k):
    if(x>=len(l) or x<0): return g
    if(y>=len(l[0]) or y<0): return g
    if(l[x][y]=='S' and not (x,y) in k): 
        g+=1
        k.append((x,y))
    if(l[x][y]=='#'): return g
    if(t==0): return g
    r.append(move(x-1,y,t-1,g,k.copy()))
    r.append(move(x+1,y,t-1,g,k.copy()))
    r.append(move(x,y-1,t-1,g,k.copy()))
    r.append(move(x,y+1,t-1,g,k.copy()))
    return g

ip=sys.stdin.readline
x,y,z=map(int,ip().strip().split())
l=[[] for _ in range(x)]
for i in range(x):
    l[i]=list(ip().strip())
s=(0,0)
for i in range(x):
    for j in range(y):
        if(l[i][j]=='G'):
            s=(i,j)
r=[]
move(s[0],s[1],z,0,[])
print(max(r))