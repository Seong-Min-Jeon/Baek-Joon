f=10**9
n=int(input())
if(n==0): print('0\n0'); exit()
if(n<0 and -n%2==0): print(-1)
else: print(1)
a=b=1
for _ in range(abs(n)-2): a,b=b,(a+b)%f
print(b)