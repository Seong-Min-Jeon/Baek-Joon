import math
I=input
n=int(I())
x=[*map(int,I().split())]
y=[*map(int,I().split())]
a,b,c,m=1e9,0,1,1
for i in range(n):
    if(b*x[i]<a*y[i]): a,b,c,m=x[i],y[i],1,1
    elif(b*x[i]==a*y[i]): a,b=x[i],y[i]; c+=1; m=max(m,c)
    else: c=0
g=math.gcd(a,b)
print(b//g,a//g)
print(m)