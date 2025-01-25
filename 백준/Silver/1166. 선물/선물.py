n,l,w,h=map(int,input().split())
x,z=0,max(l,w,h)
for _ in range(10**4):
    y=(x+z)/2    
    if((l//y)*(w//y)*(h//y)<n): z=y
    else: x=y
print(x)