from itertools import product as P
from copy import deepcopy as D
def f(i,j):
    for a,b in ((1,0),(-1,0),(0,1),(0,-1),(0,0)):
        if(0<=i+a<10 and 0<=j+b<10):
            t[i+a][j+b]='#' if t[i+a][j+b]=='O' else 'O'
l=[list(input().strip()) for _ in range(10)]
r=1e9
for p in P((0,1),repeat=10):
    c=0
    t=D(l)
    for j in range(10):
        if(p[j]==1):
            c+=1; f(0,j)
    for i in range(1,10):
        for j in range(10):
            if(t[i-1][j]=='O'):
                c+=1; f(i,j)
    if('O' in t[-1]): continue
    else: r=min(r,c)
print(r)