l=[0,1,2]
for _ in range(999):
    l.append(l[len(l)-1]+l[len(l)-2])
print(l[int(input())]%10007)