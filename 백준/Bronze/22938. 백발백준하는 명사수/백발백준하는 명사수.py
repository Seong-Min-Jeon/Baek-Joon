import math
a,b,c=map(int,input().split())
x,y,z=map(int,input().split())
print('YES' if math.dist((a,b),(x,y))<c+z else 'NO')