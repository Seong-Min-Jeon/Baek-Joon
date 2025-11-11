import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m=F()
j=[1]
for _ in range(m):
    a,b=F()
    if(a==1): j.append((j[-1]+b-1)%n+1)
    elif(a==2): j.append((j[-1]-b-1)%n+1)
    else: j.append(j[b])
print(j[-1])