import sys
I=sys.stdin.readline
f=lambda:map(int,I().split())
n,m=f()
l={}
for _ in range(m):
    i,j,d=f()
    if(d not in l): l[d]=[]
    l[d].append((i,j))
s,z=f()
x=[1e20]*(n+1)
y=[1e20]*(n+1)
y[s]=0
for d in sorted(l.keys()):
    e=l[d]
    for i,j in e:
        x[i]=min(x[i],y[j]+d)
        x[j]=min(x[j],y[i]+d)
    for i,j in e:
        y[i]=min(y[i],x[i])
        y[j]=min(y[j],x[j])
        x[i]=1e20
        x[j]=1e20
if(y[z]==1e20): print('DIGESTA')
else: print(y[z])