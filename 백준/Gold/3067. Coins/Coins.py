import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n=int(I())
    l=set(map(int,I().split()))
    m=int(I())
    r=[0]*(m+1)
    r[0]=1
    for v in l:
        for i in range(v,m+1):
            r[i]+=r[i-v]
    print(r[-1])