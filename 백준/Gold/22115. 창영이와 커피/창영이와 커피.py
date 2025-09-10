n,k=map(int,input().split())
l=[*map(int,input().split())]
r=[0]+[1e9]*k
for i in range(n):
    for j in range(k,l[i]-1,-1):
        r[j]=min(r[j],r[j-l[i]]+1)
print(r[-1] if r[-1]!=1e9 else -1)