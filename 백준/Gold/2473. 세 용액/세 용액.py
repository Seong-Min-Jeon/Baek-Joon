n=int(input())
l=sorted(list(map(int,input().split())))
r=10**10
a,b,c=0,0,0
for i in range(n-2):
    x,z=i+1,n-1
    while x<z:
        y=(x+z)//2
        if(abs(l[i]+l[x]+l[z])<r): r=abs(l[i]+l[x]+l[z]); a,b,c=i,x,z
        if(l[i]+l[x]+l[z]>0): z-=1
        else: x+=1
print(l[a],l[b],l[c])