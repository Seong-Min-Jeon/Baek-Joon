from collections import deque as dq
r,c=map(int,input().split())
l=[list(input().strip()) for _ in range(r)]
o,v=0,0
for i in range(r):
    for j in range(c):
        if(l[i][j]=='#'): continue
        s,w=0,0
        q=dq([(i,j)])        
        while q:
            x,y=q.popleft()            
            for n,m in ((0,0),(1,0),(-1,0),(0,1),(0,-1)):
                if(0<=x+n<r and 0<=y+m<c and l[x+n][y+m]!='#'):
                    q.append((x+n,y+m))
                    if(l[x+n][y+m]=='v'): w+=1
                    elif(l[x+n][y+m]=='o'): s+=1
                    l[x+n][y+m]='#'
        if(s>w): o+=s
        else: v+=w
print(o,v)