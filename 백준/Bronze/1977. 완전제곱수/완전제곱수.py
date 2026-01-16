a=set()
for i in range(1,101):
    a.add(i*i)
b=set()
for i in range(int(input()),int(input())+1):
    if(i in a):
        b.add(i)
if(len(b)==0): print(-1); exit()
print(sum(b))
print(min(b))