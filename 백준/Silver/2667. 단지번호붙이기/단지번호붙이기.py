n=int(input())
l=[[0 for _ in range(n+2)]]
for _ in range(n):
    t=list(map(int,input().strip()))
    t.insert(0,0)
    t.append(0)
    l.append(t)
l.append([0 for _ in range(n+2)])
v=[[0 for _ in range(n+2)] for _ in range(n+2)]
c=0
for x in range(1,n+1):
    for y in range(1,n+1):
        if(l[x][y]==1 and v[x][y]==0):
            c+=1
            q=[(x,y)]
            v[x][y]=c
            while q:
                i,j=q[0][0],q[0][1]
                q.pop(0)
                if(v[i-1][j]==0 and l[i-1][j]==1): q.append((i-1,j)); v[i-1][j]=c
                if(v[i+1][j]==0 and l[i+1][j]==1): q.append((i+1,j)); v[i+1][j]=c
                if(v[i][j-1]==0 and l[i][j-1]==1): q.append((i,j-1)); v[i][j-1]=c
                if(v[i][j+1]==0 and l[i][j+1]==1): q.append((i,j+1)); v[i][j+1]=c
m=max(max(e) for e in v)
t=[]
for i in range(m):
    t.append(sum(e.count(i+1) for e in v))
t.sort()
print(m)
for e in t:
    print(e)