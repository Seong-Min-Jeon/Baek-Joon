c,n=map(int,input().split())
l=[[*map(int,input().split())] for _ in range(n)]
r=[1e99]*(100+c)
r[0]=0
for i in range(100+c):
    for j in range(n):
        d,p=l[j]
        r[i]=min(r[i],r[i-p]+d)
print(min(r[c:]))