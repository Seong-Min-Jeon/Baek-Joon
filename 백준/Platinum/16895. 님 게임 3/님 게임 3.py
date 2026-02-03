I=input
n=int(I())
l=[*map(int,I().split())]
r=0
for i in range(n):
    r^=l[i]
c=0
for i in range(n):
    for k in range(1,l[i]+1):
        x=r
        x^=l[i]
        x^=l[i]-k
        if(x==0): c+=1
print(c)