import sys
sys.setrecursionlimit(10**6)
I=sys.stdin.readline
def f(i,p):
    if(r[-1]!=0): return
    if(i>n): return
    for e in l[i]:
        if(r[-1]!=0): break
        if(e==p or v[i+1][e]): continue
        r[i]=e
        f(i+1,e)
        v[i+1][e]=1
n=int(I())
l=[[0]]
for _ in range(n):
    _,*t=map(int,I().split())
    l.append(t)
v=[[0]*10 for _ in range(n+2)]
r=[0]*(n+1)
f(1,0)
if(r[-1]):
    for i in range(1,n+1):
        print(r[i])
else:
    print(-1)