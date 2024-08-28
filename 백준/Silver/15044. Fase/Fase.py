a=int(input())
b=int(input())
l=[]
for i in range(a):
    l.append(int(input()))
l.sort()
c=0
t=0
for i in range(len(l)):
    v=l.pop()
    if(v==t):
        c+=1
        continue
    if(c>=b-1 and t==0):
        t=v
    elif(c>=b):
        break
    c+=1
print(c)