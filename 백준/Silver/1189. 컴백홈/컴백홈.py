def f(x,y,d,c,k):
    global m
    if(d==k):
        if(x==0 and y==c-1): m+=1
        return
    for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
        if(0<=x+i<r and 0<=y+j<c and v[x+i][y+j]==0 and l[x+i][y+j]!=1):
            v[x+i][y+j]=1
            f(x+i,y+j,d+1,c,k)
            v[x+i][y+j]=0

r,c,k=map(int,input().split())
l=[[0]*c for _ in range(r)]
for i in range(r):
    for j,p in enumerate(list(input().strip())):
        if(p=='.'): l[i][j]=0
        else: l[i][j]=1
v=[[0]*c for _ in range(r)]
v[r-1][0]=1
m=0
f(r-1,0,1,c,k)
print(m)