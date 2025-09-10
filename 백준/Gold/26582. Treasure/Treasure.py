import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n,w=map(int,I().split())
    l=[tuple(map(int,I().split())) for _ in range(n)]
    r=[0]*(w+1)
    for i in range(n):
        a,b=l[i]
        for j in range(w,b-1,-1):
            r[j]=max(r[j],r[j-b]+a)
    print(r[-1])