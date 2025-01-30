n,a,d=map(int,input().split())
l=list(map(int,input().split()))
c=0
for e in l:
    if(e==a): c+=1; a+=d
print(c)