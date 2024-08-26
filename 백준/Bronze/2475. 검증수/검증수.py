a=list(map(int,input().split()))
s=0
for i in a:
    s+=i*i
print(s%10)