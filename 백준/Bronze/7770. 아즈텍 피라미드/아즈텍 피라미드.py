l=[1]
for i in range(10000):
    l.append(l[-1]+(i+1)*4)
c=0
r=int(input())
for i in range(10000):
    c+=l[i]
    if(c>r): break
print(i)