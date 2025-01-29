n=int(input())
l=[]
c=0
if(n%5==0): l.append(n//5)
while n>0:
    if(n%2==0): l.append(n//2+c)
    n-=5
    c+=1
if(len(l)==0): print(-1)
else: print(min(l))