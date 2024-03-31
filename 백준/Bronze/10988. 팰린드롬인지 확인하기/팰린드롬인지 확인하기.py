a=input()
l=len(a)
if(l%2==1):l-=1
for i in range(l):   
    if(a[i]!=a[-(i+1)]):
        print(0)
        exit()
print(1)