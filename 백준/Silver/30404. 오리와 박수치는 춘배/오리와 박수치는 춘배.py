n,k=map(int,input().split())
l=[*map(int,input().split())]
p,c=l[0]+k,1
for i in range(n):
    if(p<l[i]): p=l[i]+k; c+=1
print(c)