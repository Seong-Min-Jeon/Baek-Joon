n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
q=[(0,0)]
while q:
    x,y=q.pop(0)
    d=l[x][y]
    if(d==0): continue
    if(x==y==n-1): print('HaruHaru'); exit()
    if(x+d<n): q.append((x+d,y))
    if(y+d<n): q.append((x,y+d))
print('Hing')