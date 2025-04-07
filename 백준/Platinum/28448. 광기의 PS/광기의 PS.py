n,m=map(int,input().split())
l=[]
g,c=0,0
for _ in range(n):
    x,y=map(int,input().split())
    if(y<=5): c+=y
    else: l.append([x,y,x*y])
def f(l,m,g,c):
    for x,y,z in l:
        if(m<z+g): c+=g-(m-z); c+=y; g=m-min(z,5*x)
        else: c+=y; g+=z; g=max(0,g-min(z,5*x))    
    return c
print(min(f(sorted(l,key=lambda x:x[0]),m,g,c),
          f(sorted(l,key=lambda x:-x[0]),m,g,c),
          f(sorted(l,key=lambda x:x[1]),m,g,c),
          f(sorted(l,key=lambda x:-x[1]),m,g,c),
          f(sorted(l,key=lambda x:x[2]),m,g,c),
          f(sorted(l,key=lambda x:-x[2]),m,g,c)))