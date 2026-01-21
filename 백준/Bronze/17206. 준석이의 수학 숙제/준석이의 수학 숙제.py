l=[0]
for i in range(80001):
    if(i%3==0 or i%7==0): l.append(l[-1]+i)
    else: l.append(l[-1])
input()
r=[*map(int,input().split())]
for i in r:
    print(l[i+1])