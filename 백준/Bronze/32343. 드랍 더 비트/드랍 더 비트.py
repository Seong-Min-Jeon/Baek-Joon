n=int(input())
a,b=map(int,input().split())
r=2**n-1
if(n==a+b): print(r)
else: print(r-2**(abs(n-(a+b)))+1)