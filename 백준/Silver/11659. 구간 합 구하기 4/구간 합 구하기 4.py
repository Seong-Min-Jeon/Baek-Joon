import sys
ip=sys.stdin.readline
a,b=map(int,ip().split())
l=list(map(int,ip().split()))
m=[0]
for e in l:
    m.append(m[len(m)-1]+e)
for _ in range(b):
    c,d=map(int,ip().split())
    print(m[d]-m[c-1])