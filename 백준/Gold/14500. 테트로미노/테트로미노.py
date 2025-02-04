import sys
I=sys.stdin.readline

def f(i,j,s,v):
    global n,m
    if(len(s)==4):
        r.append(sum(s))
        return
    for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
        if(x<0 or x>=n or y<0 or y>=m): continue
        if((x,y) in v): continue
        t=s.copy()
        t.append(l[x][y])
        u=v.copy()
        u.append((x,y))
        f(x,y,t,u)

def g(i,j):
    s=l[i][j]
    for x,y in ((i,j+1),(i,j+2),(i-1,j+1)):
        if(x<0 or x>=n or y<0 or y>=m): break
        s+=l[x][y]
    r.append(s)
    s=l[i][j]
    for x,y in ((i,j+1),(i,j+2),(i+1,j+1)):
        if(x<0 or x>=n or y<0 or y>=m): break
        s+=l[x][y]
    r.append(s)
    s=l[i][j]
    for x,y in ((i+1,j),(i+2,j),(i+1,j+1)):
        if(x<0 or x>=n or y<0 or y>=m): break
        s+=l[x][y]
    r.append(s)
    s=l[i][j]
    for x,y in ((i+1,j),(i+2,j),(i+1,j-1)):
        if(x<0 or x>=n or y<0 or y>=m): break
        s+=l[x][y]
    r.append(s)

n,m=map(int,I().split())
l=[list(map(int,I().split())) for _ in range(n)]
r=[]
for i in range(n):
    for j in range(m):
        f(i,j,[l[i][j]],[(i,j)])
        g(i,j)
print(max(r))