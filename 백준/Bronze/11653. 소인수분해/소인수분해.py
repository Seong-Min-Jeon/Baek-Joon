a=int(input())
b=2
for _ in range(a+1):
    if(a==1): exit()
    if(a%b==0): 
        print(b)
        a/=b
        b=2
    else: b+=1