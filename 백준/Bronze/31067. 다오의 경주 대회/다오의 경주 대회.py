n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(1,n):
    if(l[i-1]>=l[i]): 
        l[i]+=k
        c+=1
        if(l[i-1]>=l[i]):
            print(-1); exit()
print(c)