def f():
    global m,c
    if(len(r)==k): c=max(c,m); return
    for i in range(n):
        if(i not in r):
            t=0
            for j in r:
                t+=l[i][j]
            r.append(i)            
            m+=t
            f()
            m-=t
            r.remove(i)
n,k=map(int,input().split())
l=[[*map(int,input().split())] for _ in range(n)]
r=[]
m,c=0,-1e9
f()
print(c)