import sys,math
I=sys.stdin.readline
l=[[1]]
v=[(1,1)]
for i in range(2,12):
    t=[]
    for j in range(i-1):
        t.append(v[j][0]*math.comb(i,v[j][1]))
    s=sum(t)
    t.append(s+1)
    v.append((s+1,i))
    l.append(t)
for _ in range(int(I())):
    print(sum(l[int(I())-1]))