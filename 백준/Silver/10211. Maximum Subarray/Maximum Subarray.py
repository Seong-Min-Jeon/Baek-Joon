for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=-1e9
    for i in range(n):
        t=l[i:].copy()
        for j in range(1,n-i):
            t[j]+=t[j-1]
        m=max(m,max(t))
    print(m)