import sys
i=sys.stdin.readline
a=int(i())
d=dict()
v=map(int,i().split())
for j in v:
    if(not j in d): d[j]=1; continue
    d[j]=d.get(j)+1
c=int(i())
m=list(map(int,i().split()))
for i in m:
    if(i in d):
        print(d[i], end=' ')
    else:
        print(0, end=' ')