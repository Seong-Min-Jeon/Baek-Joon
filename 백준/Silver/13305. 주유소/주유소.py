n=int(input())
d=list(map(int,input().split()))
p=list(map(int,input().split()))
i,c=0,0
while True:
    if(i==n-1): break
    for j in range(i,n):
        if(p[j]<p[i]): break
    c+=p[i]*sum(d[i:j])
    i=j
print(c)