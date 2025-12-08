while True:
    try:
        n,k=map(int,input().split())
        print(n+int((n-1)/(k-1)))
    except: break