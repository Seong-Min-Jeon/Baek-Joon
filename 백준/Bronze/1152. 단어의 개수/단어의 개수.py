a=input().split()
b=len(a)
if(b==0): print(0); exit()
if(a[0]==''): b-=1
elif(a[b-1]==''): b-=1
print(b)