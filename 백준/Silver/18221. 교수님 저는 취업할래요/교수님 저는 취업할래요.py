import sys
ip=sys.stdin.readline
a=int(ip())
l=[]
for _ in range(a):
    l.append(list(map(int,ip().split())))
p,s=(),()
b=[]
for r in range(a):
    for c in range(a):
        if(l[r][c]==5): p=(r,c)
        if(l[r][c]==2): s=(r,c)
        if(l[r][c]==1): b.append((r,c))
if((p[0]-s[0])**2+(p[1]-s[1])**2<25): print(0); exit()
c=0
for e in b:
    if(min(p[0],s[0])<=e[0] and max(p[0],s[0])>=e[0] 
       and min(p[1],s[1])<=e[1] and max(p[1],s[1])>=e[1]):
        c+=1
if(c>=3): print(1)
else: print(0)