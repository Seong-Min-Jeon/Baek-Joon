I=input
n=int(I())
l=[*map(int,I().split())]+[0]*10**6
k=int(I())
t=[]
p=[]
f=0
r=-1
for i in range(n+1):
    if(l[i]==1): t.append(i)
    elif(l[i]>1): p.append(i)
if(len(t)>2): f=1
elif(len(t)==2):
    if(t[0]+k!=t[1]): f=1
    else: r=t[0]
elif(len(t)==1): 
    if(l[t[0]+k]!=0): r=t[0]
    elif(l[t[0]-k]!=0 and l[t[0]-k]!=2): r=t[0]-k
    else: f=1
else:
    q=set(p)
    for e in p:
        if(l[e]>2 and e+k in q):
            r=e; break
    if(r<0): f=1
if(f): print('NO')
else: print('YES'); print(f'{r} {r+k}')