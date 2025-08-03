import math
def f(a,b):
    a=list(map(int,list(str(a))))
    b=list(map(int,list(str(b))))
    return 5*math.prod(sorted(a,reverse=True)[:3])+a[0]*sum(b)+min(b)
def g(t):
    if(t==b): print(k); exit()
    if(t not in v): v.add(t); s[k].add(t)
a,b=map(int,input().split())
if(a==b): print(0); exit()
s=[set() for _ in range(23)]
s[0]={a}
v={a}
for k in range(1,23):
    for i in range(k):
        j=k-i-1
        for n in s[i]:
            for m in s[j]:
                g(f(n,m))
                g(f(m,n))
print(-1)