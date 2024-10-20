import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline

def check(x,y,z):
    if(l[y][x]==1):
        global c
        if(z==1): c+=1
        l[y][x]=2
        if(x!=len(l[y])-1):
            check(x+1,y,0)
        if(y!=len(l)-1):
            check(x,y+1,0)
        if(x!=0 and z==0):
            check(x-1,y,0)
        if(y!=0 and z==0):
            check(x,y-1,0)

for _ in range(int(ip())):
    m,n,k=map(int,ip().split())
    l=[[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y=map(int,ip().split())
        l[y][x]=1
    c=0
    for x in range(m):
        for y in range(n):
            check(x,y,1)
    print(c)