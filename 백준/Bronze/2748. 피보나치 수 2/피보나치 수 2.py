a,b=0,1
n=int(input())
if(n==0): print(0)
for _ in range(n-1):
    a,b=b,a+b
print(b)