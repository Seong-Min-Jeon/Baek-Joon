import sys
I=sys.stdin.readline
n,m=map(int,I().split())
l=[]
q=[]
r=[[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):    
    t=list(map(int,I().split()))
    l.append(t)
    if(2 in t): 
        q.append((i,t.index(2),0))
        r[i][t.index(2)]=0
while q:
    t=q.pop(0)
    x,y,c=t[0],t[1],t[2]    
    for a,b in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        if(a<0 or b<0 or a>=n or b>=m): continue
        if(r[a][b]!=-1): continue
        if(l[a][b]==0): continue
        q.append((a,b,c+1))
        r[a][b]=c+1
for i in range(n):
    for j in range(m):
        if(l[i][j]==0 and r[i][j]==-1): print(0,end=' ')
        else: print(r[i][j],end=' ')
    print()