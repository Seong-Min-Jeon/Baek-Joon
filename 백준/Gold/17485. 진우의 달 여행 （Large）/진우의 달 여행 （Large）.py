f=lambda:map(int,input().split())
n,m=f()
l=[[1e9]*3]+[[e]*3 for e in f()]+[[1e9]*3]
for _ in range(n-1):
    d=[[1e9]*3]+[[e]*3 for e in f()]+[[1e9]*3]
    for i in range(1,m+1):
        d[i][0]+=min(l[i+1][1],l[i+1][2])
        d[i][1]+=min(l[i][0],l[i][2])
        d[i][2]+=min(l[i-1][0],l[i-1][1])
    l=d.copy()
print(min(min(e) for e in l))