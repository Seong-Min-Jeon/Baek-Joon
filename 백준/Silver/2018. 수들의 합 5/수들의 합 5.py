n=int(input())
x,y=1,1
s=1
c=0
while True:
    if(s==n): c+=1
    if(s<=n): y+=1; s+=y
    else: s-=x; x+=1
    if(y>n): break
print(c)