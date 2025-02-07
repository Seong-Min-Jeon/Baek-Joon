import heapq

def f(n):
    for _ in range(int(input())):
        p,q,r,s=map(int,input().split())
        for i in range(min(p,r),max(p,r)+1):
            for j in range(min(q,s),max(q,s)+1):
                l[i][j]=n

l=[[0 for _ in range(501)] for _ in range(501)]
f(1); f(2)
r=[[10**4 for _ in range(501)] for _ in range(501)]
q=[(0,0,0)]
r[0][0]=0
while q:
    d,x,y=heapq.heappop(q)
    if(r[x][y]<d): continue
    for a,b in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        if(0<=a<=500 and 0<=b<=500):
            n=l[a][b]
            if(n==2): continue
            if(r[a][b]>d+n):
                r[a][b]=d+n
                heapq.heappush(q,(d+n,a,b))
if(r[500][500]==10**4): print(-1)
else: print(r[500][500])