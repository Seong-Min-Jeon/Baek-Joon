l=[0,1,2]
i=2
for _ in range(10**3):
    for _ in range(2):
        l.append(l[-1]+l[i])    
    i+=1
for _ in range(int(input())): print(l[int(input())//2+1])