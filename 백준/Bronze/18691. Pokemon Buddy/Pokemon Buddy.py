for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if(a==2): a=3
    elif(a==3): a=5
    if(b>=c): print(0)
    else: print((c-b)*a)