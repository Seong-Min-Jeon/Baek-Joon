import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n,m,w=map(int,I().split())
    l=[]
    for _ in range(m):
        x,y,c=map(int,I().split())
        l.append((x,y,c))
        l.append((y,x,c))
    for _ in range(w):
        x,y,c=map(int,I().split())
        l.append((x,y,-c))
    for i in range(1,n+1):
        l.append((0,i,0))
    r=[0 for _ in range(n+1)]
    r[0]=0
    f=0
    for i in range(n+1):
        for j in range(len(l)):
            x,y,c=l[j]
            if(r[x]!=1e9 and r[y]>r[x]+c):
                r[y]=r[x]+c
                if(i==n and f==0):
                    print('YES')
                    f=1
    if(f==0): print('NO')