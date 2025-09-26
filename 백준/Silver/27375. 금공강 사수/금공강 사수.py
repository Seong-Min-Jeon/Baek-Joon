def f(m,i):
    global c
    if(m>r): return
    if(m==r): c+=1; return
    for j in range(i+1,n):
        x,y,z=e[j]
        if(x==5): continue
        b=0
        for k in range(y,z+1):
            if(l[x][k]==1): b=1; break
        if(b): continue
        for k in range(y,z+1): l[x][k]=1
        f(m+z-y+1,j)
        for k in range(y,z+1): l[x][k]=0
n,r=map(int,input().split())
l=[[0]*(11) for _ in range(6)]
e=[tuple(map(int,input().split())) for _ in range(n)]
c=0
f(0,-1)
print(c)