F=lambda:map(int,input().split())
a,b,c=F();x,y,z=F()
t=x-a
if(b<y or (b==y and c<=z)):print(t)
else:print(t-1)
print(t+1)
print(t)