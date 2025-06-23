n=int(input())
t=list(map(int,input().split()))
l,r=[1 if e==1 else -1 for e in t],[1 if e==2 else -1 for e in t]
m,x,y=0,0,0
for i in range(n):
    x=max(x+l[i],0)
    y=max(y+r[i],0)
    m=max(m,x,y)
print(m)