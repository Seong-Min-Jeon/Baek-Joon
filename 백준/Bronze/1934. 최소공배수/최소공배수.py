import sys
ip=sys.stdin.readline
for _ in range(int(ip())):
    s=set()
    a,b=map(int,ip().split())
    for i in range(1,min(a,b)+1):
        if(a%i==0 and b%i==0): s.add(i)
    m=max(list(s))
    print((a//m)*m*(b//m))