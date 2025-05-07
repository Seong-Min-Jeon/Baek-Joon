def f(v,i,j,x,y):
    global r,n,m
    if(v in s): r=max(r,v)
    if(0<=i+x<n and 0<=j+y<m): f(10*v+l[i+x][j+y],i+x,j+y,x,y)
s=set([i**2 for i in range(31700)])
n,m=map(int,input().split())
l=[tuple(map(int,list(input().strip()))) for _ in range(n)]
r=-1
for i in range(n):
    for j in range(m):
        for x in range(-9,10):
            for y in range(-9,10):
                if(x==y==0): continue
                f(l[i][j],i,j,x,y)
print(r)