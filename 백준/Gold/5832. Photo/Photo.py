n,k=map(int,input().split())
q=[]
for _ in range(k):
    x,y=map(int,input().split())
    if(x>y): x,y=y,x
    q.append((x,y))
q.sort(key=lambda x: x[1])
v=[0]*k
c=0
for i,(x,y) in enumerate(q):
    if(v[i]==1): continue
    c+=1
    for j in range(i+1,k):
        if(y>q[j][0]): v[j]=1
print(c+1)