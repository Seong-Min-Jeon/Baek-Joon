I=input
n,m=int(I()),int(I())
l=list(map(int,I().split()))
x,z=l[0],n
while x<=z:
    y=(x+z)//2
    t=0
    for p in l:
        if(t>=p-y): t=p+y
        else: t=-1
    if(t>=n): z=y-1
    else: x=y+1
print(x)