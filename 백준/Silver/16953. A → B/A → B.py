import sys
sys.setrecursionlimit(10**6)

def m(n,c):
    global r
    n*=2
    if(r<=c):
        return
    if(n==b):        
        r=min(r,c)
    elif(n>b):
        return
    else:
        m(n,c+1)
        p(n,c+1)

def p(n,c):
    global r
    n=n*10+1    
    if(r<=c):
        return
    if(n==b):       
        r=min(r,c)
    elif(n>b):
        return
    else:
        m(n,c+1)
        p(n,c+1)

a,b=map(int,input().split())
c,r=1,10**9
m(a,c)
p(a,c)
if(r==10**9): print(-1)
else: print(r+1)