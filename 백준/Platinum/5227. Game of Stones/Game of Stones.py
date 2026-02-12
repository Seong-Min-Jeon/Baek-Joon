import sys
from collections import defaultdict as D
I=sys.stdin.readline
F=lambda:map(int,I().split())
def f(n):
    if(n not in d): g[n]=0; return 0
    if(g[n]>=0): return g[n]
    s=set()
    for e in d[n]:
        s.add(f(e))
    for i in range(1000):
        if(i not in s):
            g[n]=i
            break
    return g[n]
while True:
    a,b=F()
    if(a==b==0): break
    l=[*F()]
    d=D(list)
    for i in range(b):
        d[l[2*i]].append(l[2*i+1])
    g=[-1]*a
    for k in range(a):
        f(k)
    x=0
    s=[*F()]
    for i in range(a):
        if(s[i]%2==1):
            x^=g[i]
    print('First' if x else 'Second')