import sys
sys.setrecursionlimit(10**6)
I=sys.stdin.readline

def d(s):
    for e in l[s]:
        if(v[e]==[]):
            v[s].append(e)
            d(e)

def f(s):
    for e in v[s]: c[s]+=f(e)
    return c[s]

n,r,q=map(int,I().split())
l=[[] for _ in range(n+1)]
for _ in range(n-1):
    x,y=map(int,I().split())
    l[x].append(y)
    l[y].append(x)
v=[[] for _ in range(n+1)]
d(r)
c=[1 for _ in range(n+1)]
f(r)
for _ in range(q):
    print(c[int(I())])