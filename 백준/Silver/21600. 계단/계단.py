n=int(input())
l=list(map(int,input().split()))
r=[1 for _ in range(n)]
for i in range(1,len(l)):
    if(l[i]>=r[i-1]+1): r[i]=r[i-1]+1
    else: r[i]=l[i]
print(max(r))