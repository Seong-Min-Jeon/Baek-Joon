M=1000000007
l=[1,1]
for _ in range(50):l.append(l[-2]+l[-1]+1)
print(l[int(input())]%M)