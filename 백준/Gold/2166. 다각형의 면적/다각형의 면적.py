import sys
I=sys.stdin.readline
l=[list(map(int,I().split())) for _ in range(int(I()))]
s=0
for i in range(len(l)-1): s+=l[i][0]*l[i+1][1]-l[i+1][0]*l[i][1]
s+=l[-1][0]*l[0][1]-l[0][0]*l[-1][1]
print(round(abs(s/2),1))