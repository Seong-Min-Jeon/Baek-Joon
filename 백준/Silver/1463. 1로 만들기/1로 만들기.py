l=[0,0,1,1]
for i in range(4,10**6+1):
    t=[]
    if(i%3==0):
        t.append(l[i//3]+1)
    if(i%2==0):
        t.append(l[i//2]+1)
    t.append(l[i-1]+1)
    l.append(min(t))
print(l[int(input())])