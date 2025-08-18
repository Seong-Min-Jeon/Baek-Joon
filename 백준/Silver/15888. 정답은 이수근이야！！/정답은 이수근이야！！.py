a,b,c=map(int,input().split())
x=(-b+(b*b-4*a*c)**0.5)/(2*a)
y=(-b-(b*b-4*a*c)**0.5)/(2*a)
s={2**i for i in range(1,200)}
t={i-1000 for i in range(2000)}
if(isinstance(x,complex)): print('둘다틀렸근'); exit()
x,y=round(x,6),round(y,6)
if(x!=y and x in s and y in s): print('이수근')
elif(x!=y and x in t and y in t): print('정수근')
else: print('둘다틀렸근')