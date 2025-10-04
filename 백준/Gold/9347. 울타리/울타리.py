import sys
from collections import deque as D
I=sys.stdin.readline
for _ in range(int(I())):
    n,m=map(int,I().split())
    l=[[-1]+list(map(int,I().split()))+[-1] for _ in range(n)]
    l.insert(0,[-1]*(m+2))
    l.append([-1]*(m+2))
    r=[[1e9]*(m+2) for _ in range(n+2)]
    r[0][0]=0
    q=D([(0,0,0)])
    while q:
        d,i,j=q.popleft()
        for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
            if(0<=x+i<n+2 and 0<=y+j<m+2):
                if(l[x+i][y+j]==1 and r[x+i][y+j]>r[i][j]+1):
                    r[x+i][y+j]=r[i][j]+1
                    q.append((1,x+i,y+j))
                elif(l[x+i][y+j]!=1 and r[x+i][y+j]>r[i][j]):
                    r[x+i][y+j]=r[i][j]
                    q.appendleft((0,x+i,y+j))
    t,c=0,0
    for i in range(n+2):
        for j in range(m+2):
            if(r[i][j]>t and l[i][j]==0): t=r[i][j]; c=1
            elif(r[i][j]==t and l[i][j]==0): c+=1
    print(t,c)