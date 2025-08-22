import sys
I=sys.stdin.readline
f=lambda:map(int,I().split())
a,q=f();l=sorted([*f()]);r=[0]
for i in range(a): r.append(r[-1]+l[i])
for _ in range(q):n,m=f();print(r[m]-r[n-1])