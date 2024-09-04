a=int(input())
c=0
for i in range(a//4+1):
    for j in range(a//5+1):
        if(i*4+j*5==a):
            c+=1
print(c)