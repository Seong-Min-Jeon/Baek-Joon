import sys,heapq
I=sys.stdin.readline
n,m=map(int,I().split())
l=[list(I().strip()) for _ in range(n)]
q=[]
r=[[1e99]*m for _ in range(n)]
s=(0,0)
for i in range(n):
    for j in range(m):
        if(l[i][j]=='G'):
            q.append((0,i,j))
            r[i][j]=0
        if(l[i][j]=='S'): s=(i,j)
while q:
    d,i,j=heapq.heappop(q)
    if(r[i][j]<d): continue
    for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
        if(0<=x+i<n and 0<=y+j<m and l[x+i][y+j]!='#'):
            c,v=0,[]
            for a,b in ((1,0),(-1,0),(0,1),(0,-1)):
                if(0<=x+i+a<n and 0<=y+j+b<m and l[x+i+a][y+j+b]=='G'):
                    c+=1
                    v.append(r[x+i+a][y+j+b])
            v.sort()
            if(c>=2 and r[x+i][y+j]>v[1]+1):
                r[x+i][y+j]=v[1]+1
                l[x+i][y+j]='G'
                heapq.heappush(q,(v[1]+1,x+i,y+j))
print(r[s[0]][s[1]] if r[s[0]][s[1]]!=1e99 else -1)