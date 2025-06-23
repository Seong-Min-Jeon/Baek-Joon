I=input; I()
t=list(map(int,I().split()))
l,r=[1 if e==1 else -1 for e in t],[1 if e==2 else -1 for e in t]
m,x,y=0,0,0
for i in range(len(t)):
 x,y=max(x+l[i],0),max(y+r[i],0)
 m=max(m,x,y)
print(m)