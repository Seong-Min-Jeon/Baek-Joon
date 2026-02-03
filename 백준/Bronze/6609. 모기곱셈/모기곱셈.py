try:
    while True:
        m,p,l,e,r,s,n=map(int,input().split())
        for _ in range(n): m,p,l=p//s,l//r,m*e
        print(m)
except: pass