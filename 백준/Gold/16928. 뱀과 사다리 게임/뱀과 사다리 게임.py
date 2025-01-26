I=input
n,m=map(int,I().split())
l,s={},{}
for _ in range(n):
    a,b=map(int,I().split())
    l[a]=b
for _ in range(m):
    a,b=map(int,I().split())
    s[a]=b
v=[0 for _ in range(101)]
v[1]=1
p,q=[],[1]
c=1
while True:    
    a=q.pop()
    for b in (a+1,a+2,a+3,a+4,a+5,a+6):
        if(b in l): b=l.get(b,b)
        if(b in s): b=s.get(b,b)
        if(b<101 and v[b]==0): v[b]=1; p.append(b)    
    if(v[100]==1): break
    if(not q): c+=1; q=p.copy(); p.clear()
print(c)