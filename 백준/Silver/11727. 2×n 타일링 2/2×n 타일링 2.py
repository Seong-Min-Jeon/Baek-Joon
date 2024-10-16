l=[0,1,3]
for _ in range(999):
    l.append(l[len(l)-1]+2*l[len(l)-2])
print(l[int(input())]%10007)