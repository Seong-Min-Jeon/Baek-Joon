import sys
ip=sys.stdin.readline
for _ in range(int(ip())):
    a=int(ip())
    m=[0 for _ in range(a)]
    n=[0 for _ in range(a)]
    x=list(map(int,ip().split()))
    y=list(map(int,ip().split()))
    for i in range(a):        
        if(i==0): m[i],n[i]=x[i],y[i]; continue
        if(i==1): m[i],n[i]=x[i]+n[i-1],y[i]+m[i-1]; continue
        m[i]=max(x[i]+n[i-1],x[i]+max(m[i-2],n[i-2]))
        n[i]=max(y[i]+m[i-1],y[i]+max(m[i-2],n[i-2]))
    print(max(m[-1],n[-1]))