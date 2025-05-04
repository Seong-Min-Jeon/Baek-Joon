for _ in range(int(input())):
    n=int(input())
    t=(n*(n+1))//2
    x,z=1,t
    while x<=z:
        y=(x+z)//2
        a=y*(y-1)
        if(t<a): z=y-1
        else: x=y+1
    print(z)