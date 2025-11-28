import sys
I=sys.stdin.readline
sys.setrecursionlimit(10**6)
def f(u):    
    for v in t[u]:
        if(w[v]==0):
            w[v]=1
            f(v)            
            r[u][0]+=r[v][1]
            r[u][1]+=min(r[v][0],r[v][1])
n=int(I())
t=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,I().split())
    t[a].append(b)
    t[b].append(a)
r=[[0,1] for _ in range(n+1)]
w=[0]*(n+1)
w[1]=1
f(1)
print(min(r[1]))