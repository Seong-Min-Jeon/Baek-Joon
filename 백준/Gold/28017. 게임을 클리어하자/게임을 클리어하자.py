import sys
I=sys.stdin.readline
n,m=map(int,I().split())
l=list(map(int,I().split()))
for _ in range(n-1):
    x=list(map(int,I().split()))
    for i in range(m):
        t=l.copy()
        del t[i]
        x[i]+=min(t)
    l=x.copy()
print(min(l))