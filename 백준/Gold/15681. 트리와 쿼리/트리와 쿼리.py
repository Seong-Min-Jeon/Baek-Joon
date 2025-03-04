import sys
sys.setrecursionlimit(10**6)
I=sys.stdin.readline
def d(s):
    for e in l[s]:
        if(v[e]==1):
            l[e].remove(s)
            v[s]+=d(e)
    return v[s]
n,r,q=map(int,I().split())
l=[[] for _ in range(n+1)]
for _ in range(n-1):
    x,y=map(int,I().split())
    l[x].append(y)
    l[y].append(x)
v=[1 for _ in range(n+1)]
d(r)
for _ in range(q):
    print(v[int(I())])