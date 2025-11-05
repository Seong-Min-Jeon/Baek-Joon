p=[1]*(10**3)
r=set()
for i in range(2,10**3):
    if(p[i]==1):
        r.add(i)
        for j in range(2*i,10**3,i):
            p[j]=0
a,b=map(int,input().split())
c,d=map(int,input().split())
x,y=set(),set()
for i in range(a,b+1):
    if(i in r):
        x.add(i)
for i in range(c,d+1):
    if(i in r):
        y.add(i)
t=0
while x and y:
    f=1
    if(t==0):
        for e in x:
            if(e in y):
                x.remove(e)
                y.remove(e)
                f=0
                break
        if(f):
            x.pop()
        t=1
    else:
        for e in y:
            if(e in x):
                x.remove(e)
                y.remove(e)
                f=0
                break
        if(f):
            y.pop()
        t=0
if(not x): print('yj')
else: print('yt')