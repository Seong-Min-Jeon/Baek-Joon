import sys,heapq
I=sys.stdin.readline
for _ in range(int(I())):
    k,w,h=map(int,I().split())
    d={}
    for _ in range(k):
        a,b=I().strip().split()
        d[a]=int(b)
    d['E']=0
    l=[list(I().strip()) for _ in range(h)]
    x,y=0,0
    for i in range(h):
        for j in range(w):
            if(l[i][j]=='E'):
                x,y=i,j
    r=[[1e99]*w for _ in range(h)]
    r[x][y]=0
    q=[(0,x,y)]
    while q:
        v,x,y=heapq.heappop(q)
        if(x==0 or y==0 or x==h-1 or y==w-1): print(v); break
        if(r[x][y]<v): continue
        for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
            if(0<=x+i<h and 0<=y+j<w and r[x+i][y+j]>d[l[x+i][y+j]]+v):
                r[x+i][y+j]=d[l[x+i][y+j]]+v
                heapq.heappush(q,(r[x+i][y+j],x+i,y+j))