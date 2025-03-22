import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n=int(I())
    l=[[0]*n for _ in range(n)]
    a,b=map(int,I().split())
    x,y=map(int,I().split())
    v=[[0]*n for _ in range(n)]
    q=[(a,b,0)]
    v[a][b]=1
    while q:
        c,d,e=q.pop(0)
        if(c==x and d==y): print(e); break
        for f,g in ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)):
            if(0<=c+f<n and 0<=d+g<n and v[c+f][d+g]==0):
                q.append((c+f,d+g,e+1))
                v[c+f][d+g]=1