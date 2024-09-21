i=input
m=int(i())*int(i())*int(i())
l=[0,0,0,0,0,0,0,0,0,0]
for e in str(m): l[int(e)]+=1
for e in l: print(e)