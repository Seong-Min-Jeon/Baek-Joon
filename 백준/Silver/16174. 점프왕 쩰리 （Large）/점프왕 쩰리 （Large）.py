n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
v=[[0]*n for _ in range(n)]
q=[(0,0)]
while q:
    x,y=q.pop(0)
    d=l[x][y]
    if(d==0): continue
    if(x+d==y==n-1 or x==y+d==n-1): print('HaruHaru'); exit()
    if(x+d<n and v[x+d][y]==0): q.append((x+d,y)); v[x+d][y]=1
    if(y+d<n and v[x][y+d]==0): q.append((x,y+d)); v[x][y+d]=1
print('Hing')