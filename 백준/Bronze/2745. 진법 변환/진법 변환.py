n,b=input().split()
b=int(b)
a=0
for i in range(len(n)):
    x=n[len(n)-1-i]    
    if(not str.isdigit(x)):
        c=ord(x)
        x=c-65+10    
    a+=int(x)*(b**i)
print(a)