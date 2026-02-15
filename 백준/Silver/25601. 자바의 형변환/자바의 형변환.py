import sys
from collections import defaultdict as D
def f(a):
    global g
    for e in d[a]:
        if(e==x or e==y): g=1
        f(e)
I=sys.stdin.readline
n=int(I())
d=D(list)
for _ in range(n-1):
    a,b=I().split()
    d[b].append(a)
x,y=I().split()
g=0
f(x)
f(y)
print(1 if g else 0)