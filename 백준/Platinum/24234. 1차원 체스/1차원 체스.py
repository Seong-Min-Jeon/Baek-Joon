import sys
sys.setrecursionlimit(10**6)
I=sys.stdin.readline
def f(d,l):
    l.pop(0)
    for e in l:
        if(e not in d): d[e]={}
        d=d[e]
    d['*']=d.get('*',0)+1
def g(d):
    global c
    for r in d:
        if(not isinstance(d[r],int)):
            if(len(d[r])>1):
                t=[]
                for e in d[r]:
                    h(d[r][e])
                    t.append(c)
                    c=0
                z=0
                for e in t: z+=e**2
                l[r]+=(sum(t)**2-z)//2
            g(d[r])
def h(d):
    global c
    if(isinstance(d,int)): return
    for r in d:
        if(r=='*'): c+=d[r]
        else: h(d[r])
n,q=map(int,I().split())
d={}
for _ in range(n): f(d,list(map(int,I().split())))
l=[0]*10001
c=0
g(d)
for _ in range(q): print(l[int(I())])