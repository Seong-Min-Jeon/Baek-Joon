n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
w=0
x,y,z=0,l[-1]//2,l[-1]
while True:
    t=[]
    for e in l:
        if(y<e): t.append(e-y)
    if(sum(t)==m): print(y); exit()
    elif(sum(t)<m): y,z=(x+y)//2,y
    else: x,y=y,(y+z)//2
    if(x==y or y==z): print(y); exit()