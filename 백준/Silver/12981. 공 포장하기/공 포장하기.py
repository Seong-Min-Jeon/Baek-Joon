r,g,b=map(int,input().split())
c=min(r,g,b)
r-=c; g-=c; b-=c
c+=r//3; r%=3
c+=g//3; g%=3
c+=b//3; b%=3
if(r+g+b>2): c+=2
elif(r+g+b==0): pass
else: c+=1
print(c)