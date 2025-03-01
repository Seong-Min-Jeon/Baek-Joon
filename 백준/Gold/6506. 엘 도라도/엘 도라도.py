import sys
I=sys.stdin.readline
while True:
    n,k=map(int,I().split())
    if(n==0): break
    l=list(map(int,I().split()))
    r=[[0 for _ in range(n)] for _ in range(k)]
    for i in range(n):
        r[0][i]=1
    for i in range(1,k):
        for j in range(n):
            s=0
            for m in range(j):
                if(l[m]<l[j]):
                    s+=r[i-1][m]
            r[i][j]=s
    print(sum(r[-1]))