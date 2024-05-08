i=input
while(True):
    a,b,c=map(int,input().split())
    if(a==b==c==0): break
    if(a+b+c<=2*max(a,b,c)): print('Invalid'); continue
    if(a==b==c): print('Equilateral')
    elif(a==b or a==c or b==c): print('Isosceles')
    else: print('Scalene')