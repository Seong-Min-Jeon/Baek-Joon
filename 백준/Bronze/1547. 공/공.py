p=1
for _ in range(int(input())):
    a,b=map(int,input().split())
    if(a==p): p=b
    elif(b==p): p=a
print(p)