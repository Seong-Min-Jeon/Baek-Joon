import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n=int(I())
    a,b=map(int,I().split())
    l=[tuple(map(int,I().split())) for _ in range(n)]
    x,y=map(int,I().split())
    if(abs(a-x)+abs(b-y)<=1000): print('happy'); continue
    v=[0]*n
    q=[(a,b)]
    while q:
        c,d=q.pop(0)
        f=0
        for z,(i,j) in enumerate(l):
            if(abs(c-i)+abs(d-j)<=1000 and v[z]==0):
                if(abs(i-x)+abs(j-y)<=1000): print('happy'); f=1; break
                v[z]=1
                q.append((i,j))
        if(f): break
    if(not f): print('sad')