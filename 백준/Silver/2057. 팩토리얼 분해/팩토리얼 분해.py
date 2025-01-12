from itertools import combinations as c
l=[1]
for i in range(1,20):
    l.append(l[-1]*i)
s=set()
for i in range(1,21):
    for e in c(l,i):
        s.add(sum(e))
a=int(input())
if(a in s): print('YES')
else: print('NO')