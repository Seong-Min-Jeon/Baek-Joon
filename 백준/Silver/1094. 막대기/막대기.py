a=int(input())
l=[64]
while True:
    if(sum(l)==a): break
    b=l.pop()
    l.append(b//2)
    if(sum(l)<=a): l.append(b//2)
print(len(l)-l.count(0))