l=list(map(int,input().split()))
m=[1,1,2,2,2,8]
for i in range(6):
    m[i]=m[i]-l[i]
print(*m)