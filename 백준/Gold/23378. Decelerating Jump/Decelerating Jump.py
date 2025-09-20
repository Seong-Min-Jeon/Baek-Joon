n=int(input())
l=[*map(int,input().split())]
r=[-1e99]*n
r[-1]=l[-1]
for k in range(1,n):
    for i in range(n-k-1,-1,-1):
        r[i]=max(r[i],r[i+k]+l[i])
print(r[0])