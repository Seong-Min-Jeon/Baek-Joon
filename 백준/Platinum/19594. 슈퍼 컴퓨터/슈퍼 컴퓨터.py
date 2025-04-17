import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n=int(I())
    h=list(map(int,I().split()))
    d=list(map(int,I().split()))
    l=[(i,j) for i,j in zip(h,d)]
    l.sort(key=lambda x:x[1])
    s=0
    r=[]
    for a,b in l: s+=a; r.append(max(0,s-b))
    m=1e9
    x=0
    for i in range(n):
        if(l[i][0]<=x): continue
        x=l[i][0]
        t=r.copy()
        for j in range(i,n):
            t[j]-=l[i][0]-1
        m=min(m,max(t))
    print(max(0,m))