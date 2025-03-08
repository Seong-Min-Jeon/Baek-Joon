import sys
import math
I=sys.stdin.readline

def g(p):
    if(p==0): return 0
    s=1
    q=[p]
    while q:
        c=q.pop(0)
        if(l[c][0]!=0):
            s+=1
            q.append(l[c][0])
        if(l[c][1]!=0):
            s+=1
            q.append(l[c][1])
    return s

def f(p):
    if(l[p][0]==0 and l[p][1]==0): return 1
    x,y=g(l[p][0]),g(l[p][1])
    return (f(l[p][0])*f(l[p][1])*(math.factorial(x+y)//(math.factorial(x)*math.factorial(y))))%9999991

for _ in range(int(I())):
    l=[[0,0] for _ in range(int(I())+1)]
    r=0
    for e in list(map(int,I().split())):
        if(r==0): r=e; continue
        t=r
        while True:
            if(t<e): 
                c=l[t][1]
                if(c==0): l[t][1]=e; break
                else: t=c
            else: 
                c=l[t][0]
                if(c==0): l[t][0]=e; break
                else: t=c
    print(f(r))