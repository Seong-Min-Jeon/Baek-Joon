x=input().strip()
if(x.startswith('0x')): print(int(x,base=16))
elif(x.startswith('0')): print(int(x,base=8))
else: print(x)