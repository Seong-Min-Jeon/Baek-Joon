l=[]
m=[]
for _ in range(3):
    a,b=input().split()    
    if(a in l): l.remove(a)
    else: l.append(a)
    if(b in m): m.remove(b)
    else: m.append(b)
print(l[0], m[0])