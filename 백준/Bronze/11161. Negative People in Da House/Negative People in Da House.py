for _ in range(int(input())):
    m,s=0,0
    for _ in range(int(input())):
        a,b=map(int,input().split())
        s+=a-b
        m=min(m,s)
    print(-m)