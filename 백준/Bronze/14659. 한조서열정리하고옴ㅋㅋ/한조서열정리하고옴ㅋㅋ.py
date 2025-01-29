n=int(input())
l=list(map(int,input().split()))
m=0
for i,e in enumerate(l):
    t=0
    for j in range(i+1,n):
        if(l[j]>e): break
        t+=1
    m=max(m,t)
print(m)