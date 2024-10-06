import sys
ip=sys.stdin.readline
a,b=map(int,ip().split())
m={}
l=[]
for _ in range(a):
    c,d=ip().split()
    m[c]=d
for _ in range(b):
    l.append(ip().strip())
for e in l:
    print(m.get(e))