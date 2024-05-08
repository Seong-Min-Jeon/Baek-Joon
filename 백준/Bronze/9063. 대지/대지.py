i=int(input())
l,m=[],[]
for _ in range(i):
    a,b=map(int,input().split())
    l.append(a)
    m.append(b)
if(i<2): print(0); exit()
l.sort()
m.sort()
print((l[-1]-l[0])*(m[-1]-m[0]))