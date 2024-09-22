n=int(input())
c=0
if(n==1): print(n); exit()
for i in range(20):
    if(n<2**i+1): print(2*(n-2**(i-1)-1)+2); exit()