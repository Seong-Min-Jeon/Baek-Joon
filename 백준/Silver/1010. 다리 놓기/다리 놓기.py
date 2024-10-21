for _ in range(int(input())):
    n,m=map(int,input().split())
    t,b=1,1
    for i in range(m,m-n,-1):
        t*=i
    for i in range(1,n+1):
        b*=i    
    print(t//b)