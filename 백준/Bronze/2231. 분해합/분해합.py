a=int(input())
b=0
for i in range(a,0,-1):
    t=i
    for j in str(i):        
        t+=int(j)
    if(a==t):
        b=i
print(b)