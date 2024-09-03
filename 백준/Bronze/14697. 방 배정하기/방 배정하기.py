a,b,c,n=map(int,input().split())
v=0
for i in range(n//a+1):
    for j in range(n//b+1):
        for k in range(n//c+1):            
            if(n==i*a+j*b+k*c):
                print(1)
                exit(0)
print(0)