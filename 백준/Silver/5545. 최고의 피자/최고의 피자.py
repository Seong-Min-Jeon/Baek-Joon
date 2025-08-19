l=[*map(int,open(0).read().split())]
print(max([int((l[3]+sum(sorted(l[4:],reverse=True)[:i]))/(l[1]+l[2]*i)) for i in range(l[0]+1)]))