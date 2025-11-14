F=lambda:map(int,input().split())
n,m=F()
l=[[1e9]*n for _ in range(n)]
for _ in range(m):
  a,b,c=F()
  a-=1;b-=1
  l[a][b]=c
r=1e9
for k in range(n):
  l[k][k]=0
  for i in range(n):
    for j in range(n):
      t=l[i][k]+l[k][j]
      l[i][j]=min(l[i][j],t)
      if(i==j and i!=k): r=min(r,t)
print(r if r!=1e9 else -1)