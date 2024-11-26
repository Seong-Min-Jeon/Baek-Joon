a=int(input())
l=list(map(int,input().split()))
r=[0 for _ in range(a)]
for i in range(a):
    r[i]=l[i]
    for j in range(i):
        if(l[j]<l[i]):
            r[i]=max(r[i],r[j]+l[i])
print(max(r))