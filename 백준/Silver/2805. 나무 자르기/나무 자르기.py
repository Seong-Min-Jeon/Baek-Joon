n,m=map(int,input().split())
l=list(map(int,input().split()))
x,y,z=0,max(l)//2,max(l)
while True:
    t = sum(e-y for e in l if y<e)
    if(t<m): y,z=(x+y)//2,y
    else: x,y=y,(y+z)//2
    if(x==y or y==z): print(y); break