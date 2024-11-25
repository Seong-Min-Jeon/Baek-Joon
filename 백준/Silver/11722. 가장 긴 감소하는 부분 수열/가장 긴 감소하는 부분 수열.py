a=int(input())
l=list(map(int,input().split()))
r=[0 for _ in range(a)]
for i in range(a):
    r[i]=1
    for j in range(i):
        if(l[j]>l[i]):
            r[i]=max(r[i],r[j]+1)
print(max(r))