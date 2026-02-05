l=[0]*1001
l[0],l[1],l[2]=0,0,1
for i in range(3,1001):
    s=set()
    for j in range(i-2):
        t=l[j]^l[i-j-2]
        s.add(t)
    for k in range(1000):
        if(k not in s):
            l[i]=k
            break
print(1 if l[int(input())]!=0 else 2)