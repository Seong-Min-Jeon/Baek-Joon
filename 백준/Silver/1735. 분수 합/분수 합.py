a,b=map(int,input().split())
c,d=map(int,input().split())
x=b
y=d
while y>0:
    x,y=y,x%y
x=b*d//x
a=a*(x//b)
c=c*(x//d)
e,f=a+c,x
x=e
y=f
while y>0:
    x,y=y,x%y
e=e//x
f=f//x
print(e,f)