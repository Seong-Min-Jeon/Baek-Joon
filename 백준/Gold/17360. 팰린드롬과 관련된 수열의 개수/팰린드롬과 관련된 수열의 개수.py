import math
n,m,k=map(int,input().split())
M=1000000007
if(n==k and n%2==0): print(pow(m,n//2,M))
elif(n==k): print(pow(m,n//2,M)*m%M)
elif(k==1 or n<k): print(pow(m,n,M))
elif(k%2==0): print(m)
else: print(m+math.comb(m,2)*2)