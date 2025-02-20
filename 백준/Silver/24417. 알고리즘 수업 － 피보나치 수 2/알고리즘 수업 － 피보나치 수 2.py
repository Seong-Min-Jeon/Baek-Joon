n=int(input())
f=1000000007
a,b=1,1
for i in range(n-2): a,b=b,(a+b)%f
print(b,(n-2)%f)