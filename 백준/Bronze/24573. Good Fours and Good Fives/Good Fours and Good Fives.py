a=int(input())
c=0
for i in range(a//4+1):
    if((a-i*4)%5==0):
        c+=1
print(c)