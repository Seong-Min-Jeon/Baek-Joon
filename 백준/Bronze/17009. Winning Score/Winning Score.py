a=0
for i in range(3):
    a+=int(input())*(3-i)
b=0
for i in range(3):
    b+=int(input())*(3-i)
if(a>b): print('A')
elif(a<b): print('B')
else: print('T')