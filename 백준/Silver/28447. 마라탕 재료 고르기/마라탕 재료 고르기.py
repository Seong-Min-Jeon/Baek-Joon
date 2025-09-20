def f(m,r):
    global c
    if(len(r)==k): c=max(c,m); return
    for i in range(n):
        if(not r or r[-1]<i):
            t=0
            for j in r:
                t+=l[i][j]
            f(m+t,r+[i])
n,k=map(int,input().split())
l=[[*map(int,input().split())] for _ in range(n)]
c=-1e9
f(0,[])
print(c)