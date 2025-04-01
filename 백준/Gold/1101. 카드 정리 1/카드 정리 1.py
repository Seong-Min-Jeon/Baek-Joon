n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
r=1e9
for k in range(n):
    v=[0]*m
    c=0
    for i in range(n):
        if(i==k): continue
        t=[]
        for j in range(m):
            if(l[i][j]!=0): t.append(j)
        if(len(t)>1): c+=1
        elif(len(t)==0): continue
        elif(v[t[0]]==0): v[t[0]]=1
        else: c+=1
    r=min(r,c)
print(r)