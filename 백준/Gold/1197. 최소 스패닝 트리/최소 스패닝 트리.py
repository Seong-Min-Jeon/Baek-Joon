import sys
sys.setrecursionlimit(10**6)
I=sys.stdin.readline
def f(a):
    if(p[a]!=a): p[a]=f(p[a])
    return p[a]
v,e=map(int,I().split())
q=[]
for _ in range(e):
    a,b,c=map(int,I().split())
    q.append((c,a,b))
q.sort(reverse=True)
p=[i for i in range(v+1)]
s=0
while q:
    c,a,b=q.pop()    
    x,y=f(a),f(b)
    if(x==y): continue
    p[x],p[y]=min(x,y),min(x,y)
    s+=c
print(s)