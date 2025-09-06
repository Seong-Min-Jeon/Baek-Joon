import sys
I=sys.stdin.readline
f=lambda:map(int,I().split())
n,m=f()
l=[]
for _ in range(n):
    v,c,k=f()
    t=1
    while k>=t:
        l.append((v*t,c*t))
        k-=t
        t*=2
    l.append((v*k,c*k))
r=[0]*(m+1)
for i in range(len(l)):
    v,c=l[i]
    for j in range(m,v-1,-1):
        r[j]=max(r[j],r[j-v]+c)
print(r[-1])