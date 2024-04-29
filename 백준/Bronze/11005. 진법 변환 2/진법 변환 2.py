def d(n):
    if(n>9): return chr(55+n)
    return n

a,b=map(int,input().split())
c=''
while a>=b:
    c+=str(d(a%b))
    a=a//b    
c+=str(d(a))    
print(c[::-1])