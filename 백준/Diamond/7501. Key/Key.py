def is_prime(n):
    if(n<2): return 0
    A=(2,3,5,7,11,13,17,19,23,29,31,37)
    for p in A:
        if(n%p==0): return n==p
    d,s=n-1,0
    while d%2==0:
        d//=2
        s+=1
    for a in A:
        x=pow(a,d,n)
        if(x==1) or (x==n-1): continue
        for _ in range(s-1):
            x=x*x%n
            if(x==n-1): break
        else:
            return 0
    return 1

l=[]
a,b=map(int,input().split())
for i in range(a,b+1):
    if(i==2): continue
    if(i==9): l.append(i)
    if(is_prime(i)): l.append(i)
print(*l)