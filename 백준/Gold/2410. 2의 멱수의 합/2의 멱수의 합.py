l=[1]
for i in range(1,(int(input())//2)+1): l.append((l[-1]+l[i//2])%1000000000)
print(l[-1])