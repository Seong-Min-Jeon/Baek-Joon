while True:
    try:
        n,k=map(int,input().split())
        r=n
        while n>=k:
            r+=n//k
            n=n-k*(n//k)+n//k
        print(r)
    except: break