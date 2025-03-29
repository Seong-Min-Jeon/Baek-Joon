l=[0]*10**5
l[0],l[1]=1,1
for i in range(2,10**5):
    if(l[i]==1): continue
    for j in range(i*2,10**5,i): l[j]=1
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    if(0 not in l[a:b+1]): print(-1); continue
    v=[0]*(10**6+1)
    q=[(n,0)]
    f=0
    while q:
        m,c=q.pop(0)
        if(a<=m<=b and l[m]==0): print(c); break
        for e in (2,3):
            if(0<=m//e<=10**6 and v[m//e]==0): q.append((m//e,c+1)); v[m//e]=1
        for e in (1,-1):
            if(0<=m+e<=10**6 and v[m+e]==0): q.append((m+e,c+1)); v[m+e]=1