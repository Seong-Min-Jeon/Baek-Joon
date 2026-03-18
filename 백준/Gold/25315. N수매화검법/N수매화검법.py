import sys
from collections import defaultdict as D
I=sys.stdin.readline
def f(a,b,x,y,n,m): return (a*y+x*m+n*b)-(a*m+x*b+n*y)
def g(p,q):
    a,b,c,d,_=p
    w,x,y,z,_=q
    if(f(a,b,c,d,w,x)*f(a,b,c,d,y,z)<0 and f(w,x,y,z,a,b)*f(w,x,y,z,c,d)<0): return True
    return False
n=int(I())
l=[tuple(map(int,I().split())) for _ in range(n)]
m=[0]*n
d=D(set)
for i in range(n):
    for j in range(i+1,n):
        if(g(l[i],l[j])): m[i]+=1; m[j]+=1; d[i].add(j); d[j].add(i)
r=[]
for i in range(n):
    r.append((l[i][4],m[i],i))
r.sort()
x=0
s=set()
for w,m,i in r:
    for e in d[i]:
        if(e in s): m-=1
    x+=(m+1)*w
    s.add(i)
print(x)