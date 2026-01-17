import sys
I=sys.stdin.readline
d={}
for s in range(1555):
    d[s]=sum([i*(s) for i in range(s)])
for _ in range(int(I())):
    a,b=map(int,I().split())
    print(d[a+b])