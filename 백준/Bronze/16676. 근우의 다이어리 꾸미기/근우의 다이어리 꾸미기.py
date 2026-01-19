n=int(input())
c='1'
while True:
    if(n>=int(c)): c+='1'
    else: break
print(len(c)-1 if n!=0 else 1)