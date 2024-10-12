import sys
ip=sys.stdin.readline
for _ in range(int(ip())):
    m={}
    t=1
    for _ in range(int(ip())):
        s=ip().split()[1]
        m[s]=m.get(s,1)+1
    for v in m.values():
        t*=v
    print(t-1)