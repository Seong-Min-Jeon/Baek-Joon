def f(s,p,c):
    global m
    m=max(m,s)
    if(c>=k): return
    if(p<n): f(s+l[p+1],p+1,c+1)
    if(p+1<n): f(s//2+l[p+2],p+2,c+1)
I=input
F=lambda:map(int,I().split())
n,k=F()
l=[0]+[*F()]
m=0
f(1,0,0)
print(m)