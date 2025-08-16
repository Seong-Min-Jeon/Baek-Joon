l=[input() for _ in range(6)]
t=l.count('W')
if(t>4): print(1)
elif(t>2): print(2)
elif(t>0): print(3)
else: print(-1)