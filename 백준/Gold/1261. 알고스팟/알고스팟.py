import heapq
n,m=map(int,input().split())
l=[list(map(int,list(input()))) for _ in range(m)]
r=[[1e9 for _ in range(n)] for _ in range(m)]
q=[(0,0,0)]
r[0][0]=0
while q:
    s,x,y=heapq.heappop(q)
    for i,j in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        w=0
        if(0<=i<m and 0<=j<n):
            if(l[i][j]==1): w+=1
            if(r[i][j]>s+w):
                r[i][j]=s+w
                heapq.heappush(q,(s+w,i,j))
print(r[-1][-1])