import sys,heapq,math
I=sys.stdin.readline
F=lambda:map(int,I().split())
def f(r):
    while q:
        d,p=heapq.heappop(q)
        if(r[p]<d): continue
        for i,e in l[p]:
            if(r[i]>d+e):
                r[i]=d+e
                heapq.heappush(q,(d+e,i))
n,k=F()
s=[int(I()) for _ in range(k)]
l=[[] for _ in range(n+1)]
for _ in range(n-1):
    u,v,w=F()
    l[u].append((v,w))
    l[v].append((u,w))
r=[1e99]*(n+1)
r[0]=0
q=[]
for e in s:
    r[e]=0
    q.append((0,e))
f(r)
v=[1e99]*(n+1)
v[1]=0
q=[(0,1)]
f(v)
x=[1e99]*(n+1)
a,b=0,0
for e in s:
    if(v[e]>b):
        a,b=e,v[e]
x[a]=0
q=[(0,a)]
f(x)
y=[1e99]*(n+1)
a,b=0,0
for e in s:
    if(x[e]>b):
        a,b=e,x[e]
y[a]=0
q=[(0,a)]
f(y)
a,b=0,1
for i in range(n+1):
    if(a/b<r[i]/max(x[i],y[i])):
        a,b=r[i],max(x[i],y[i])
g=math.gcd(a,b)
print(f'{a//g}/{b//g}')