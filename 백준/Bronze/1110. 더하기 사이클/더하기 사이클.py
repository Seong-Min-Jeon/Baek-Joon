a=int(input())
l=[0,0]
if(a<10): l[0]=0; l[1]=a
else: l[0]=a//10; l[1]=a%10
c=0
while True:
    l[0],l[1]=l[1],(l[0]+l[1])%10
    c+=1
    if(l[0]*10+l[1]==a): break
print(c)