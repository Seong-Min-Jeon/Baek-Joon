for _ in range(3):
    a,b,c,d,e,f=map(int,input().split())
    d-=a
    e-=b
    f-=c
    if(f<0):
        e-=1
        f+=60
    if(e<0):
        d-=1
        e+=60
    print(d,e,f)