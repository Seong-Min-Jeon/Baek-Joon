n,x,y=map(int,input().split())
l=[*map(int,input().split())]
a,b=0,0
for e in l:
    c=e//x
    d=max(0,min(e%x-c*(y-x),e%x))
    a+=c
    b+=d
print(a)
print(b)