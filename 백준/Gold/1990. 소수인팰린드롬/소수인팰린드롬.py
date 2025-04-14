n,m=map(int,input().split())
r=[]
p=[1]*(9989900)
p[0],p[1]=0,0
for i in range(2,len(p)):
    if(p[i]==0): continue
    r.append(i)
    for j in range(2*i,len(p),i):
        p[j]=0
for e in r:    
    if(n<=e<=m and str(e)==str(e)[::-1]):
        print(e)
print(-1)