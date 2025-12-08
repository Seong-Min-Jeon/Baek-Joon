import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
n=int(I())
l=[*F()]
for k in range(1,n+1):
    r,s=0,-1
    for i in range(n-k+1):        
        t=l[i:i+k]
        m=sum(t)/k
        d=(sum([(e-m)**2 for e in t])/k)**0.5
        if(s<d and abs(s-d)>1e-9): r,s=i+1,d
    print(r)