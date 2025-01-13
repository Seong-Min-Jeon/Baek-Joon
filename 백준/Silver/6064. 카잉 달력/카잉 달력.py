import sys
I=sys.stdin.readline
for _ in range(int(I())):
    m,n,a,b=map(int,I().split())
    p=set([i*m+a for i in range(n+1)])
    q=set([i*n+b for i in range(m+1)])
    print(min(p&q or[-1]))