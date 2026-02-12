l=[1]
for i in range(250001):l+=[i+1]*2
l=l[:int(input())]
print(len(set(l)))
print(*l)