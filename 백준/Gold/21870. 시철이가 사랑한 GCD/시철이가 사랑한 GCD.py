import math
def f(l,s):
    if(len(l)==1): return s+l[0]
    a=l[:len(l)//2]
    b=l[len(l)//2:]
    return max(f(b,s+math.gcd(*a)),f(a,s+math.gcd(*b)))
input()
print(f(list(map(int,input().split())),0))