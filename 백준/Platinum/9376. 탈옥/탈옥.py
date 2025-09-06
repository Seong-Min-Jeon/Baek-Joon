import sys
from collections import deque as D
I=sys.stdin.readline
for _ in range(int(I())):
    n,m=map(int,I().split())
    l=[]
    for _ in range(n):
        l.append(['.']+list(I().strip())+['.'])
    l=[['.']*(m+2)]+l+[['.']*(m+2)]
    r=[[[1e9]*(m+2) for _ in range(n+2)] for _ in range(3)]
    q=D([(0,0,0,0)])
    r[0][0][0]=0
    c=1
    for i in range(n+2):
        for j in range(m+2):
            if(l[i][j]=='$'):
                q.append((0,i,j,c))
                r[c][i][j]=0
                c+=1
    while q:
        d,i,j,c=q.popleft()
        for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
            if(0<=x+i<n+2 and 0<=y+j<m+2):
                if((l[x+i][y+j]=='.' or l[x+i][y+j]=='$') and r[c][x+i][y+j]>d):
                    r[c][x+i][y+j]=d
                    q.appendleft((d,x+i,y+j,c))
                elif(l[x+i][y+j]=='#' and r[c][x+i][y+j]>d+1):
                    r[c][x+i][y+j]=d+1
                    q.append((d+1,x+i,y+j,c))
    z=1e9
    for i in range(n+2):
        for j in range(m+2):
            t=2 if l[i][j]=='#' else 0
            z=min(z,r[0][i][j]+r[1][i][j]+r[2][i][j]-t)
    print(z)