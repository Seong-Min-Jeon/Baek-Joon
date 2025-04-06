def m(x,y):
    global M
    t=[0]*4
    t[0]=((x[0]*y[0])%M+(x[1]*y[2])%M)%M
    t[1]=((x[0]*y[1])%M+(x[1]*y[3])%M)%M
    t[2]=((x[2]*y[0])%M+(x[3]*y[2])%M)%M
    t[3]=((x[2]*y[1])%M+(x[3]*y[3])%M)%M
    return t

def f(n):
    if(n<=1): return [1,1,1,0]
    t=f(n//2)
    if(n%2==0): return m(t,t)
    else: return m(m(t,t),[1,1,1,0])

M=1000000007
print(f(int(input()))[1])