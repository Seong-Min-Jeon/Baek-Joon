import copy
def f(l,n,s):
    global m
    for i in range(len(l)):
        for j in range(len(l)):
            l[i][j][1]=0
            m=max(m,l[i][j][0])            
    if(n==5): return
    f(a(l),n+1,s+'u')
    f(b(l),n+1,s+'d')
    f(c(l),n+1,s+'l')
    f(d(l),n+1,s+'r')

def a(l):
    t=copy.deepcopy(l)
    n=len(t)
    for _ in range(n):
        for i in range(1,n):
            for j in range(n):
                if(t[i-1][j][0]==t[i][j][0] and t[i][j][0]!=0 and t[i-1][j][1]==0 and t[i][j][1]==0):
                    t[i-1][j]=[2*t[i][j][0],1]
                    t[i][j][0]=0
                elif(t[i-1][j][0]==0 and t[i][j][0]!=0):
                    t[i-1][j][0]=t[i][j][0]
                    t[i][j][0]=0
    return t

def b(l):
    t=copy.deepcopy(l)
    n=len(t)
    for _ in range(n):
        for i in range(n-2,-1,-1):
            for j in range(n):
                if(t[i][j][0]==t[i+1][j][0] and t[i][j][0]!=0 and t[i+1][j][1]==0 and t[i][j][1]==0):
                    t[i+1][j]=[2*t[i][j][0],1]
                    t[i][j][0]=0
                elif(t[i+1][j][0]==0 and t[i][j][0]!=0):
                    t[i+1][j][0]=t[i][j][0]
                    t[i][j][0]=0
    return t

def c(l):
    t=copy.deepcopy(l)
    n=len(t)
    for _ in range(n):
        for i in range(n):
            for j in range(1,n):
                if(t[i][j-1][0]==t[i][j][0] and t[i][j][0]!=0 and t[i][j-1][1]==0 and t[i][j][1]==0):
                    t[i][j-1]=[2*t[i][j][0],1]
                    t[i][j][0]=0
                elif(t[i][j-1][0]==0 and t[i][j][0]!=0):
                    t[i][j-1][0]=t[i][j][0]
                    t[i][j][0]=0
    return t

def d(l):
    t=copy.deepcopy(l)
    n=len(t)
    for _ in range(n):
        for i in range(n):
            for j in range(n-2,-1,-1):
                if(t[i][j][0]==t[i][j+1][0] and t[i][j][0]!=0 and t[i][j+1][1]==0 and t[i][j][1]==0):
                    t[i][j+1]=[2*t[i][j][0],1]
                    t[i][j][0]=0
                elif(t[i][j+1][0]==0 and t[i][j][0]!=0):
                    t[i][j+1][0]=t[i][j][0]
                    t[i][j][0]=0
    return t

n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        l[i][j]=[l[i][j],0]
m=0
f(l,0,'')
print(m)