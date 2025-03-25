n=int(input())
l=list(map(int,input().split()))
r=10**10
a,b=0,0
for i in range(n-1):
    x,z=i+1,n-1
    while x<=z:
        y=(x+z)//2
        if(l[i]+l[y]>0): z=y-1
        else: x=y+1
    if(x==n): x-=1
    if(abs(l[i]+l[x])<r):
        r=abs(l[i]+l[x])
        a,b=i,x
    if(z==i): z+=1
    if(abs(l[i]+l[z])<r):
        r=abs(l[i]+l[z])
        a,b=i,z
print(l[a],l[b])