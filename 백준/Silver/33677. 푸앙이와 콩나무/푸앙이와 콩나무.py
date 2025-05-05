from collections import deque as dq
n=int(input())
if(n==0): print(0,0); exit()
q=dq([(0,0,0)])
v=[1e9]*1000001
r=[]
while q:
    h,c,d=q.popleft()
    if(r and r[0][0]<d+1): break
    for x,y,z in ((h+1,c+1,d+1),(h*3,c+3,d+1),(h**2,c+5,d+1)):
        if(x==n): r.append((z,y))
        if(x<=n and v[x]>y): q.append((x,y,z)); v[x]=y
print(*sorted(r)[0])