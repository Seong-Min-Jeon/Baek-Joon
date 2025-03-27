from itertools import product as p
s=input().strip()
for i in range(10):
    for l in list(p(['A','C','G','T'],repeat=i)):
        if(''.join(l) not in s):
            print(''.join(l))
            exit()