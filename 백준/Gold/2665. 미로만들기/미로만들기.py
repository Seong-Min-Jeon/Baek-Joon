from collections import deque as D;I=input
n=int(I());l,r=[list(I().strip()) for _ in range(n)],[[1e9]*n for _ in range(n)];r[0][0]=0;q=D([(0,0)])
while q:
 x,y=q.popleft()
 for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
  a,b=x+i,y+j
  if 0<=a<n and 0<=b<n:
   c=l[a][b]=='0'
   if r[a][b]>r[x][y]+c:
    r[a][b]=r[x][y]+c
    q.append((a,b)) if c else q.appendleft((a,b))
print(r[-1][-1])