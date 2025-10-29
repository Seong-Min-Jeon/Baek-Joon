import math
a,b,c,d,e=map(int,input().split())
print(min(math.ceil(a/b)*c,math.ceil(a/d)*e))