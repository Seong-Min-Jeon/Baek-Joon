import math
def f(l,s):
    if(len(l)==1):        
        r.append(s+l[0])
        return
    a=l[:len(l)//2]
    b=l[len(l)//2:]
    f(b,s+math.gcd(*a))
    f(a,s+math.gcd(*b))
n=input()
r=[]
f(list(map(int,input().split())),0)
print(max(r))