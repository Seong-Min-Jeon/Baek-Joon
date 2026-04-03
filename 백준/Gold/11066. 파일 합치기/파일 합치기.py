import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n=int(I())
    l=[*map(int,I().split())]
    s=[0]
    for i in range(n):
        s.append(s[-1]+l[i])
    d=[[1e99]*n for _ in range(n)]
    for g in range(1,n+1):
        for i in range(n-g+1):
            j=i+g-1
            if(i==j): d[i][i]=0
            for k in range(i,j):
                d[i][j]=min(d[i][j],d[i][k]+d[k+1][j]+s[j+1]-s[i])
    print(d[0][-1])