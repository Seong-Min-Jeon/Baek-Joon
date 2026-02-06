f=[1,1]
for _ in range(31):
    f.append(f[-1]+f[-2])
l=[0]*3000001
for i in range(3000001):
    s=set()
    for j in f:
        if(i>=j):
            s.add(l[i-j])
    for k in range(1000):
        if(k not in s):
            l[i]=k
            break
input()
p=[*map(int,input().split())]
x=0
for e in p:
    x^=l[e]
print('cubelover' if x==0 else 'koosaga')