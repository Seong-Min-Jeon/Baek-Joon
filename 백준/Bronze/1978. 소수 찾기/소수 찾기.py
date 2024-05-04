i=input
a=int(i())
b=list(map(int,i().split()))
c=0
for n in b:
    if(n==1): c+=1; continue
    for j in range(2,n):
        if(n%j==0): c+=1; break
print(a-c)