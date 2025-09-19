import sys
from collections import defaultdict as D
I=sys.stdin.readline
d={}
n,m=map(int,I().split())
for _ in range(n):
    a,b=I().strip().split()
    d[a]=int(b)
e=D(list)
x=D(int)
for _ in range(int(I())):
    a,b=I().strip().split()
    e[a].append(int(b))
    x[a]+=1
for k in e.keys():
    if(max(e[k])>d[k]):
        m-=max(e[k])-d[k]
        d[k]=max(e[k])
if(m<0): print(0); exit()
l=[]
for k in x.keys():
    l.append((x[k],k))
l.sort(reverse=True)
p=0
for i in range(len(l)):
    if(i==0): p=l[i][0]
w=[]
for k in e.keys():
    if(max(e[k])==d[k]): w.append(((max(e[k])+1)*e[k].count(max(e[k])),k))
    else: w.append((len(e[k]),k))
w.sort(reverse=True)
for i in range(len(w)):
    if(m==0): break
    if(w[i][0]>=p):
        m-=1
        d[w[i][1]]+=1
d[l[0][1]]+=m
r=0
for k in e.keys():
    for t in e[k]:
        if(t<d[k]):
            r+=d[k]
print(r)