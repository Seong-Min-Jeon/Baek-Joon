while True:
    n,k=map(int,input().split())
    if(n==k==0): break
    d=[[0]*n for _ in range(k+1)]
    l=list(map(int,input().split()))
    for i in range(1,k+1):
        for j in range(i-1,n):
            if(i==1): d[i][j]=1; continue
            s=0
            for h in range(j):
                 if(l[j]>l[h]):
                    s+=d[i-1][h]
            d[i][j]=s
    print(sum(d[-1]))