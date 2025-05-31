l=[int(input()) for _ in range(5)]
for i in range(5):
    l[i]=max(40,l[i])
print(sum(l)//5)