import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
for _ in range(int(I())):
    n,m=F()
    l=[[*F()] for _ in range(m)]
    l.sort(key=lambda x:x[1])
    r=[0]+[1e99]*n
    for i in range(m):
        s,p,o=l[i]
        for j in range(n,-1,-1):
            if(s+j>=n):
                r[n]=min(r[n],r[j]+p*(n-j)+o)
            if(j>=s):
                r[j]=min(r[j],r[j-s]+p*s+o)
    print(r[-1])