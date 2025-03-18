import sys
sys.setrecursionlimit(10**6)
I=sys.stdin.readline
def f(a):
    if(p[a]!=a): p[a]=f(p[a])
    return p[a]
n,m=map(int,I().split())
l=[]
for _ in range(m):
    a,b,c=map(int,I().split())
    l.append((c,a,b))
p=[i for i in range(n+1)]
l.sort(reverse=True)
r=[]
while l:
    c,a,b=l.pop()
    x,y=f(a),f(b)
    if(x!=y):
        p[x],p[y]=min(x,y),min(x,y)
        r.append(c)
r.sort()
r.pop()
print(sum(r))