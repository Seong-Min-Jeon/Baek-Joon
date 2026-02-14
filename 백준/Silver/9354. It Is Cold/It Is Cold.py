import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n=int(I())
    d=[*map(int,I().split())][::-1]
    s=list(I().strip().split())[::-1]
    t=0
    for i in range(n):
        if(s[i]=='A'): t=max(0,t-d[i])
        else: t+=d[i]
    print(t)