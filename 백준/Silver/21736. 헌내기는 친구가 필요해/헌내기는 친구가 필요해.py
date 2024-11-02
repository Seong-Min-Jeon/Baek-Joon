import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline

def s(x,y):
    global c
    if(x<0 or y<0): return
    if(x>=a or y>=b): return
    if(v[x][y]==1): return 
    v[x][y]=1
    if(m[x][y]=='X'): return
    if(m[x][y]=='P'): c+=1
    s(x+1,y)
    s(x-1,y)
    s(x,y+1)
    s(x,y-1)

a,b=map(int,ip().split())
v=[[0 for _ in range(b)] for _ in range(a)]
m=[]
for _ in range(a):
    m.append(list(ip().strip()))
x,y=0,0
for i in range(a):
    for j in range(b):
        if(m[i][j]=='I'):
            x,y=i,j
c=0
s(x,y)
if(c==0): print('TT')
else: print(c)