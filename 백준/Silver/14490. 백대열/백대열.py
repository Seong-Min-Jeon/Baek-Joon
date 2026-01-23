import math
a,b=input().strip().split(':')
a,b=int(a),int(b)
t=math.gcd(a,b)
print(f'{a//t}:{b//t}')