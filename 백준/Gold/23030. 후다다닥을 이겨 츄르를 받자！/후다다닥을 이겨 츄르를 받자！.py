import heapq
import copy
l=[[] for _ in range(int(input())+1)]
for i,x in enumerate(map(int,input().split())):
    l[i+1]=[1e9 for _ in range(x+1)]
m={}
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    m[(a,b)]=(c,d)
    m[(c,d)]=(a,b)
for _ in range(int(input())):
    v=copy.deepcopy(l)    
    t,a,b,c,d=map(int,input().split())
    q=[(0,a,b)]
    v[a][b]=0
    while q:
        e,x,y=heapq.heappop(q)
        if(v[x][y]<e): continue
        for i in (-1,1):
            if(0<y+i<len(v[x]) and v[x][y+i]>e+1): v[x][y+i]=e+1; heapq.heappush(q,(e+1,x,y+i))        
        if((x,y) in m):
            z,w=m[(x,y)]
            if(v[z][w]>e+t): v[z][w]=e+t; heapq.heappush(q,(e+t,z,w))    
    print(v[c][d])