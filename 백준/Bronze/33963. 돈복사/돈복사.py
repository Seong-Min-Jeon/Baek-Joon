n=int(input())
c=0
for _ in range(100):
    if(len(str(n))==len(str(2*n))):
        c+=1
    else: break
    n*=2
print(c)