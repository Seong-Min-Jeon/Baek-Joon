a,b=map(int,input().split())
l,r=[],[]
for i in range(a):
    p,s=map(int,input().split())
    l.append([p+s,p,s])
    r.append([p,s,p//2+s])
l.sort()
m=0
for i in range(a):
    f=0
    for j in range(a):
        if(r[i][2]>b): break
        if(r[i][0]==l[j][1] and r[i][1]==l[j][2] and f==0): f=1; continue
        r[i][2]+=l[j][0]
        m=max(m,j+1-f)
    if(r[i][2]<=b): m=max(m,j+2-f)
print(m)