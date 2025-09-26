import sys
from collections import deque as D
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m,k=F()
a,b,c=set(F()),set(F()),set(F())
l=[1e9]*(10**5+2)
r=[1e9]*(10**5+2)
l[0]=0
q=D([(0,0)])
while q:
    x,y=q.popleft()
    if(x==0):
        if(y<=10**5 and y in a and l[y+1]>l[y]+1):
            l[y+1]=l[y]+1
            q.append((0,y+1))
        if(y<=10**5 and y not in a and l[y+1]>l[y]):
            l[y+1]=l[y]
            q.appendleft((0,y+1))
        if(y>0 and y-1 in a and l[y-1]>l[y]+1):
            l[y-1]=l[y]+1
            q.append((0,y-1))
        if(y>0 and y-1 not in a and l[y-1]>l[y]):
            l[y-1]=l[y]
            q.appendleft((0,y-1))
        if(y in c and r[y]>l[y]+1):
            r[y]=l[y]+1
            q.append((1,y))
    else:
        if(y<=10**5 and y in b and r[y+1]>r[y]+1):
            r[y+1]=r[y]+1
            q.append((1,y+1))
        if(y<=10**5 and y not in b and r[y+1]>r[y]):
            r[y+1]=r[y]
            q.appendleft((1,y+1))
        if(y>0 and y-1 in b and r[y-1]>r[y]+1):
            r[y-1]=r[y]+1
            q.append((1,y-1))
        if(y>0 and y-1 not in b and r[y-1]>r[y]):
            r[y-1]=r[y]
            q.appendleft((1,y-1))
        if(y in c and l[y]>r[y]+1):
            l[y]=r[y]+1
            q.append((0,y))
print(r[int(I())])