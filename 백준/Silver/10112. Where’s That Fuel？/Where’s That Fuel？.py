n,p=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
c=1
m=l[p-1][0]
del l[p-1]
l.sort(key=lambda x: x[1])
for i in range(n-1):
    if(m<l[i][1]): break
    if(l[i][0]<l[i][1]): continue
    c+=1
    m=m+l[i][0]-l[i][1]
print(m)
print(c)