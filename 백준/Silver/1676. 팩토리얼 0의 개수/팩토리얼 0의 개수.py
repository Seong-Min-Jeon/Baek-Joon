import math
s=str(math.factorial(int(input())))
c=0
for e in s[::-1]:
    if(e=='0'): c+=1
    else: break
print(c)