I=input
n=int(I())
l=[*map(int,I().split())]
c=0
for i in range(n):    
    for k in range(1,l[i]+1):
        x=0
        for j in range(n):
            t=l[j]
            if(i==j): t-=k
            x^=t
        if(x==0): c+=1
print(c)