for _ in range(int(input())):
    a,b=map(int,input().split())
    print(10 if pow(a,b,10)==0 else pow(a,b,10))