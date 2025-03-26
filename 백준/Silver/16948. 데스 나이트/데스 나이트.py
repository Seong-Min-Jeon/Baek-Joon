n=int(input())
a,b,x,y=map(int,input().split())
v=[[-1]*n for _ in range(n)]
q=[(a,b,0)]
while q:
    i,j,d=q.pop(0)
    for r,s in ((-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)):
        if(0<=i+r<n and 0<=j+s<n and v[i+r][j+s]==-1):
            v[i+r][j+s]=d+1
            q.append((i+r,j+s,d+1))
print(v[x][y])