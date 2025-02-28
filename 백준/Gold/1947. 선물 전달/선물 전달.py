a,b=0,1
for i in range(3,int(input())+2): a,b=b,((i-1)*(a+b)%10**9)
print(a)