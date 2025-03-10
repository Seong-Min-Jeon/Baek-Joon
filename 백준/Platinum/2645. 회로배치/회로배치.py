import heapq
import sys
I=sys.stdin.readline
n=int(I())
l=[[0]*(n+1) for _ in range(n+1)]
a,b,x,y=map(int,I().split())
k=int(I())
m=int(I())
for _ in range(m):
    t=list(map(int,I().split()))
    c=t.pop(0)
    p,q=t.pop(0),t.pop(0)
    for _ in range(c-1):
        v,w=t.pop(0),t.pop(0)
        if(p==v):
            for i in range(min(q,w),max(q,w)+1): l[p][i]=1
        else:
            for i in range(min(p,v),max(p,v)+1): l[i][q]=1
        p,q=v,w
c=1
if(l[a][b]==1): c=k
if(a==x and b==y):
    print(c)
    print(2,a,b,x,y)
    exit()
q=[(c,a,b)]
p=[[(0,0)]*(n+1) for _ in range(n+1)]
t=[[1e9]*(n+1) for _ in range(n+1)]
while q:    
    c,r,s=heapq.heappop(q)
    if(r==x and s==y): break
    if(t[r][s]<c): continue
    for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
        if(n>=r+i>0 and n>=s+j>0):
            if(l[r+i][s+j]==1 and c+k<t[r+i][s+j]):
                heapq.heappush(q,(c+k,r+i,s+j))
                p[r+i][s+j]=(r,s)
                t[r+i][s+j]=c+k
            elif(l[r+i][s+j]==0 and c+1<t[r+i][s+j]):
                heapq.heappush(q,(c+1,r+i,s+j))
                p[r+i][s+j]=(r,s)
                t[r+i][s+j]=c+1
print(t[x][y])
i,j=p[x][y]
l=[(x,y)]
while i!=a or j!=b:
    l.append((i,j))
    i,j=p[i][j]
l.append((a,b))
d=0
c=[]
a,b=l.pop()
while l:
    r,s=l.pop()
    if(a+1==r and d!=1): c.append((a,b)); d=1
    elif(a-1==r and d!=2): c.append((a,b)); d=2
    elif(b+1==s and d!=3): c.append((a,b)); d=3
    elif(b-1==s and d!=4): c.append((a,b)); d=4
    a,b=r,s
c.append((x,y))
print(len(c),end=' ')
for i,j in c:
    print(i,j,end=' ')