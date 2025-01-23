def f(i,j):
    global a
    q=[(i,j,l[i][j])]
    v[i][j]=1
    while q:
        c,d,e=q.pop()
        for x,y in [(c-1,d),(c+1,d),(c,d-1),(c,d+1)]:
            if(x>=0 and x<n and y>=0 and y<n and l[x][y]==e and v[x][y]==0):
                q.append((x,y,l[x][y]))
                v[x][y]=1
    a+=1

def g(i,j):
    global b
    q=[(i,j,l[i][j])]
    w[i][j]=1
    while q:
        c,d,e=q.pop()
        for x,y in [(c-1,d),(c+1,d),(c,d-1),(c,d+1)]:
            if(x>=0 and x<n and y>=0 and y<n and w[x][y]==0):
                if((e=='R' and l[x][y]=='G') or (e=='G' and l[x][y]=='R') or (e==l[x][y])):
                    q.append((x,y,l[x][y]))
                    w[x][y]=1
    b+=1

n=int(input())
l=[list(input()) for _ in range(n)]
v=[[0 for _ in range(n)] for _ in range(n)]
w=[[0 for _ in range(n)] for _ in range(n)]
a,b=0,0
for i in range(n):
    for j in range(n):
        if(v[i][j]==0): f(i,j)
        if(w[i][j]==0): g(i,j)
print(a,b)