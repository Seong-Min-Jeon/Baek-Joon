n,m=map(int,input().split())
l=list(map(int,input().split()))
x,z=0,max(l)
while x<=z:
    y=(x+z)//2
    t=sum(e-y for e in l if y<e)
    if(t<m): z=y-1
    else: x=y+1
print(z)