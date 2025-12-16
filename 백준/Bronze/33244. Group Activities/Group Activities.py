import sys,math
I=sys.stdin.readline
r=1
for _ in range(int(I())):
  r=math.lcm(r,int(I()))
print(r)