import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
I()
f=[*F()]
for _ in range(int(I())):
    a,*b=F()
    if(a==1):
        l,r,k=b
        print(f[l-1:r].count(k))
    else:
        l,r=b
        f[l-1:r]=[0]*(r-l+1)