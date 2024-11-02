def f(n):
    if(n==0 or n==1):
        return 1
    return n*f(n-1)
n=int(input())
print(f(n))