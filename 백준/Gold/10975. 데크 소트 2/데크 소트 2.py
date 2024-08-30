def near(l:list,i:int,m:int):
    l.append(m)
    l.sort()
    if(abs(l.index(i)-l.index(m))==1):
        return True
    return False

l=[]
s=[]
a=int(input())
for i in range(a):
    l.append(int(input()))
for i in l.copy():
    if(len(s)==0):
        s.append([i])
        l.remove(i)
        continue
    k=0
    for j in s:
        if(i>max(j) and near(l.copy(),i,max(j))):
            j.append(i)            
            k=1
            break
        if(i<min(j) and near(l.copy(),i,min(j))):
            j.insert(0,i)
            k=1
            break
    if(k==0):
        s.append([i])
    l.remove(i)
print(len(s))