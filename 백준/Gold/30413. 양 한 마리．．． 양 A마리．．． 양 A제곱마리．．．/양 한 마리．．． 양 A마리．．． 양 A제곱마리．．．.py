a,b=map(int,input().split())
M=1000000007
r=pow(a,b,M)
if(a==1): print(b%M)
else: print(((r-1)*pow(a-1,M-2,M))%M)