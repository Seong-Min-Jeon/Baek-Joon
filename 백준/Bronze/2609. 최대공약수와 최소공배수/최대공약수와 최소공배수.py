a,b=map(int,input().split())
m=a*b
while b>0:
    a,b=b,a%b
print(a)
print(m//a)